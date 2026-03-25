import tkinter as tk
import csv
from datetime import datetime

root = tk.Tk()
root.title("Trading App")
root.geometry("400x400")

title = tk.Label(root, text=" Trading System", font=("Arial", 16))
title.pack(pady=10)

def place_trade():
    new_window = tk.Toplevel(root)
    new_window.title("Place Trade")
    new_window.geometry("300x400")

    tk.Label(new_window, text="Stock Name").pack()
    stock = tk.Entry(new_window)
    stock.pack()

    tk.Label(new_window, text="Trade Type (BUY/SELL)").pack()
    trade_type = tk.Entry(new_window)
    trade_type.pack()

    tk.Label(new_window, text="Entry Price").pack()
    entry = tk.Entry(new_window)
    entry.pack()

    tk.Label(new_window, text="Exit Price").pack()
    exit_price = tk.Entry(new_window)
    exit_price.pack()

    tk.Label(new_window, text="Stoploss").pack()
    sl = tk.Entry(new_window)
    sl.pack()

    tk.Label(new_window, text="Take Profit").pack()
    tp = tk.Entry(new_window)
    tp.pack()

    def save_trade():
        stock_val = stock.get()
        type_val = trade_type.get()
        entry_val = float(entry.get())
        exit_val = float(exit_price.get())
        sl_val = float(sl.get())
        tp_val = float(tp.get())

        # profit calculation
        if type_val.upper() == "BUY":
            profit = exit_val - entry_val
        else:
            profit = entry_val - exit_val

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # save to CSV
        with open("trade_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                time, stock_val, type_val,
                entry_val, exit_val, sl_val, tp_val, profit
            ])

        print("Trade Saved ")

    tk.Button(new_window, text="Save Trade", command=save_trade).pack(pady=10)

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Trade History")
    history_window.geometry("400x400")

    try:
        with open("trade_log.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                tk.Label(history_window, text=str(row)).pack()
    except:
        tk.Label(history_window, text="No trades found").pack()

def exit_app():
    root.destroy()

btn1 = tk.Button(root, text="Place Trade", command=place_trade, width=20)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Trade History", command=show_history, width=20)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Exit", command=exit_app, width=20)
btn3.pack(pady=10)

root.mainloop()
