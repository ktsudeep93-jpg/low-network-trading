import tkinter as tk

root = tk.Tk()
root.title("trading app")
root.geometry("400x400")

title = tk.Label(root,text="trading system ",font=("arial",16))
title.pack(pady=10)

def place_trade():
    print("place trade clicked ")
def show_history():
    print("history clicked")
def exit_app():
    root.destroy()

btnl = tk.Button(root,text="place trade ",command = place_trade , width=20)
btnl.pack(pady=10)

btn2 = tk.Button(root,text="trade history",commond = show_history,width=20)
btn2.pack(pady=10)

btn3 = tk.Button(root,text="exit",commond=exit_app,width=20)
btn3.pack(pady=10)

