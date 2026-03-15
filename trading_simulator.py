import random
import time

print("WELCOME TO LOW NETWORK TRADING FLATFORM ")

support = float(input("enter the support zone price : "))
resistance = float(input("enter the resistance zone price : "))

prices = []
trades = []

while True :
    price = random.randint(int(support-10),int(resistance+10))
    prices.append(price)
    print("current price " , price )
    if price > resistance :
        print("BUY SIGNAL ")
    elif price < support :
        print("SELL SIGNAL ")
    else :
        print("MARKET IN SIDEWAYS-WAIT ")

    choice = input("do you want to place an order (yes/no) : ")
    if choice == 'yes':
        stock = input("enter the stock name : ")
        entry = float(input("enter the entry price : "))
        exit_price = float(input("enter the exit price : "))
        stoploss = float(input("enter the stoploss: "))
        take_profit = float(input("enter the take profit : "))

        if exit_price <= stoploss:
            print("STOPLOSS HIT ")

        elif exit_price >= take_profit :
            print("TARGET HIT!")
            profit = take_profit - entry
        else :
            profit = exit_price - entry

        trade = {
            "stock" : stock,
            "entry" : entry ,
            "exit_price" : exit_price,
            "stoploss" : stoploss,
            "take_profit" : take_profit,
            "profit" : profit
            }
        trades.append(trade)
        print("your order is placed and saved ")
        print("order history ")
        for t in trades:
            print("----------------------")
            print("stock name : ",t["stock"])
            print("entry price : ",t["entry"])
            print("exit price : ",t["exit_price"])
            print("stoploss is : ",t["stoploss"])
            print("take profit is : ",t["take_profit"])
            print("profit is : ",t["profit"])
        print("recent price : ",prices[-5:])
        print("--------------------------------")

        time.sleep(2)
