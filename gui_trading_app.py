import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import matplotlib.pyplot as plt

app = tk.Tk()
app.title("LOW NETWORK PLATFORM")
app.geometry("400x400")

tk.Label(app, text="Market System", font=("Arial", 16)).pack(pady=10)

def trade_place():
    inside_app = tk.Toplevel(app)
    inside_app.title("Place Trade")
    inside_app.geometry("300x400")

    tk.Label(inside_app, text="Stock name").pack()
    stock = tk.Entry(inside_app)
    stock.pack()

    tk.Label(inside_app, text="Trade type").pack()
    trade_type = tk.StringVar()
    trade_type.set("BUY")
    tk.OptionMenu(inside_app, trade_type, "BUY", "SELL").pack()

    tk.Label(inside_app, text="Entry price").pack()
    entry = tk.Entry(inside_app)
    entry.pack()

    tk.Label(inside_app, text="Exit price").pack()
    exit_price = tk.Entry(inside_app)
    exit_price.pack()

    tk.Label(inside_app, text="Stoploss").pack()
    stoploss = tk.Entry(inside_app)
    stoploss.pack()

    tk.Label(inside_app, text="Take profit").pack()
    take_profit = tk.Entry(inside_app)
    take_profit.pack()

    def clear_fields():
        stock.delete(0, tk.END)
        entry.delete(0, tk.END)
        exit_price.delete(0, tk.END)
        stoploss.delete(0, tk.END)
        take_profit.delete(0, tk.END)

    def save_trade():
        try:
            stock_val = stock.get()
            type_val = trade_type.get()
            entry_val = float(entry.get())
            exit_val = float(exit_price.get())
            stoploss_val = float(stoploss.get())
            takeprofit_val = float(take_profit.get())

            if not stock_val:
                messagebox.showerror("Error", "Fill all fields")
                return

            if type_val == "BUY":
                profit = exit_val - entry_val
            else:
                profit = entry_val - exit_val

            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("trade_log.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    time, stock_val, type_val,
                    entry_val, exit_val,
                    stoploss_val, takeprofit_val, profit
                ])

            messagebox.showinfo("Success", "Trade Saved!")
            clear_fields()

        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(inside_app, text="Save Trade", command=save_trade).pack(pady=10)
    tk.Button(inside_app, text="Clear", command=clear_fields).pack()


# ------------------ TRADE HISTORY + SEARCH + GRAPH ------------------ #
def show_history():
    history_window = tk.Toplevel(app)
    history_window.title("Trade History")
    history_window.geometry("900x500")

    headers = ["Time", "Stock", "Type", "Entry", "Exit", "SL", "TP", "Profit"]

    for j, header in enumerate(headers):
        tk.Label(history_window, text=header, bg="black", fg="white", width=12)\
            .grid(row=0, column=j)

    search_var = tk.StringVar()

    tk.Label(history_window, text="Search").grid(row=0, column=8)
    search_entry = tk.Entry(history_window, textvariable=search_var)
    search_entry.grid(row=1, column=8)

    profits = []

    def load_data():
        for widget in history_window.winfo_children():
            if int(widget.grid_info().get("row", 0)) > 1 and int(widget.grid_info().get("column", 0)) < 8:
                widget.destroy()

        try:
            with open("trade_log.csv", "r") as file:
                reader = csv.reader(file)

                search_text = search_var.get().lower()

                for i, row in enumerate(reader, start=2):

                    if search_text:
                        if search_text not in row[1].lower() and search_text not in row[2].lower():
                            continue

                    for j, value in enumerate(row):
                        color = "black"

                        if j == 7:
                            try:
                                profit_val = float(value)
                                profits.append(profit_val)

                                if profit_val > 0:
                                    color = "green"
                                elif profit_val < 0:
                                    color = "red"
                            except:
                                pass

                        tk.Label(
                            history_window,
                            text=value,
                            fg=color,
                            borderwidth=1,
                            relief="solid",
                            width=12
                        ).grid(row=i, column=j)

        except:
            tk.Label(history_window, text="No Data").grid(row=2, column=0)

    tk.Button(history_window, text="Search", command=load_data)\
        .grid(row=2, column=8)

    def show_graph():
        if len(profits) > 0:
            plt.plot(profits)
            plt.title("Profit Graph")
            plt.xlabel("Trades")
            plt.ylabel("Profit")
            plt.show()
        else:
            messagebox.showinfo("Info", "No data")

    tk.Button(history_window, text="Show Graph", command=show_graph)\
        .grid(row=3, column=8)

    load_data()


def exit_app():
    app.destroy()


tk.Button(app, text="Place Order", command=trade_place, width=20).pack(pady=10)
tk.Button(app, text="Trade History", command=show_history, width=20).pack(pady=10)
tk.Button(app, text="Exit", command=exit_app, width=20).pack(pady=10)

app.mainloop()
