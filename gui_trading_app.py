import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

app = tk.Tk()
app.title("LOW NETWORK PLATFORM")
app.geometry("400x400")

title = tk.Label(app, text="Market System", font=("Arial", 16))
title.pack(pady=10)


def trade_place():
    inside_app = tk.Toplevel(app)
    inside_app.title("Place Trade")
    inside_app.geometry("300x400")

    tk.Label(inside_app, text="Stock name").pack()
    stock = tk.Entry(inside_app)
    stock.pack()

    tk.Label(inside_app, text="Trade type (buy/sell)").pack()
    trade_type = tk.Entry(inside_app)
    trade_type.pack()

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

    def save_trade():
        try:
            stock_val = stock.get()
            type_val = trade_type.get()
            entry_val = float(entry.get())
            exit_val = float(exit_price.get())
            stoploss_val = float(stoploss.get())
            takeprofit_val = float(take_profit.get())

            # Profit logic
            if type_val.lower() == "buy":
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

            messagebox.showinfo("Success", "Trade Saved Successfully!")

            stock.delete(0, tk.END)
            trade_type.delete(0, tk.END)
            entry.delete(0, tk.END)
            exit_price.delete(0, tk.END)
            stoploss.delete(0, tk.END)
            take_profit.delete(0, tk.END)

        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(inside_app, text="Save Trade", command=save_trade).pack(pady=10)


def show_history():
    history_window = tk.Toplevel(app)
    history_window.title("Trading History")
    history_window.geometry("700x400")

    headers = ["Time", "Stock", "Type", "Entry", "Exit", "SL", "TP", "Profit"]

    for j, header in enumerate(headers):
        tk.Label(history_window, text=header, bg="black", fg="white", width=12)\
            .grid(row=0, column=j)

    try:
        with open("trade_log.csv", "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader, start=1):
                for j, value in enumerate(row):
                    tk.Label(
                        history_window,
                        text=value,
                        borderwidth=1,
                        relief="solid",
                        width=12
                    ).grid(row=i, column=j)

    except:
        tk.Label(history_window, text="No trades found").pack()


def exit_app():
    app.destroy()

btn1 = tk.Button(app, text="Place Order", command=trade_place, width=20)
btn1.pack(pady=10)

btn2 = tk.Button(app, text="Trade History", command=show_history, width=20)
btn2.pack(pady=10)

btn3 = tk.Button(app, text="Exit", command=exit_app, width=20)
btn3.pack(pady=10)


app.mainloop()
