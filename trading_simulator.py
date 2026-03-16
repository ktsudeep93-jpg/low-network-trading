import random
import time

print("WELCOME TO LOW NETWORK SIMULATOR ")

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

    choice = input("ENTER YOUR CHOICE ")
    if choice == '1':
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
        file = open("trade_log.txt","a")
        file.write(stock + " " + str(entry) + " " + str(exit_price)+ " "+str(profit)+"\n")
        file.close()
        print("trade saved to file")
    elif choice == '2':
        try:
            file = open("trade_log.txt","r")
            print("saved trades ")
            file.close()
        except:
            print("no trade history found ")
        for t in trades:
            print("----------------------")
            print("stock name : ",t["stock"])
            print("entry price : ",t["entry"])
            print("exit price : ",t["exit_price"])
            print("stoploss is : ",t["stoploss"])
            print("take profit is : ",t["take_profit"])
            print("profit is : ",t["profit"])
        total_profit = 0
        for t in trades :
            total_profit += t["profit"]

        total_trades = len(trades)

        print("TOTAL TRADES : ",total_trades)
        print("TOTAL PROFIT : ",total_profit)

        print("recent prices : ",prices[-5:])
        print("--------------------------------")

        time.sleep(2)
