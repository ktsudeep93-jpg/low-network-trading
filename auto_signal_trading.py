import random
import time
import csv

print("WELCOME TO LOW NETWORK TRADING PLATFORM ")

support = float(input("enter the support price : "))
resistance = float(input("enter the resistance price : "))

prices = []
trades = []
with open("trade_log.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["stock","type","entry","exit","stoploss","takeprofit","profit"])

while True :
    print("--------MENU---------")
    print("1.place trade ")
    print("2.trading history ")
    print("3.exit ")

    choice = input("enter your choice : ")

    if choice == '1':
        price = random.randint(int(support-10),int(resistance+10))
        prices.append(price)

        print("current price is : ",price )

        if price <= support+2:
            print("BUY SIGNAL ")
            trade_type = "BUY"
        elif price >= resistance-2 :
            print("SELL SIGNAL ")
            trade_type = "SELL"
        else :
            print("WAIT CHART IN SIDE WISE")
            trade_type = "WAIT"
        print("suggested trade type is : ",trade_type )
        stock = input("enter the stock name : ")
        entry = float(input("enter the entry price : "))
        exit_price = float(input("enter the exit price : "))
        stoploss = float(input("enter the stoploss : "))
        take_profit = float(input("enter the take profit price : "))

        if exit_price >= take_profit:
            print("your target hits ")
            profit = take_profit - entry

        elif exit_price <= take_profit:
            print("your stoploss hits ")
            profit = stoploss - entry
        else :
            profit = exit_price - entry
        trade =  {
           "name": stock,
           "trade_type": trade_type,
           "entry": entry,
           "exit_price": exit_price,
           "stoploss": stoploss,
           "take_profit": take_profit,
           "profit": profit
        }
        trades.append(trade)
        with open("trade_log.csv ","a" , newline="") as file:
            writer = csv.writer(file)
            writer.writerow({
                stock,
                trade_type,
                entry,
                exit_price,
                stoploss,
                take_profit
                })
            print("trade saved to CSV!")
    elif choice== '2':
        print("trade history ")
        if len(trades) == 0:
            print("no trades yet " )
        for t in trades:
            print("-------------------")
            print("Stock:", t["name"])
            print("Type:", t["trade_type"])
            print("Entry:", t["entry"])
            print("Exit:", t["exit_price"])
            print("Stoploss:", t["stoploss"])
            print("Take Profit:", t["take_profit"])
            print("Profit:", t["profit"])
        total_profit = 0
        for t in trades:
            total_profit += t["profit"]

        print("total trade : ",len(trades))
        print("total profit : ",total_profit )

    elif choice == '3':
        print("exit program " )
        break
    else :
        print("oops! invalid input ")
    print("recent price : ",prices[-5:])
    print("----------------------------")

    time.sleep(2)
        
                      
        
