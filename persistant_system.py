import random
import time
import csv

print("WELCOME TO LOW NETWORK TRADING " )

support = float(input("enter the support zone price : "))
resistance = float(input("enter the resistance zone price : "))

prices = []
trades = []

try:
    with open("trade_log.csv","r") as file:
        reader = csv.reader(file)
        next(reader)

    for row in reader:
        trade = {
            "name" : row[0],
            "trade_type" : row[1],
            "entry" : float(row[2]),
            "exit_price" : float(row[3]),
            "stoploss" : float(row[4]),
            "take_profit" : float(row[5]),
            "profit" : float(row[6])
            }
        trades.append(trade)

    print("previous trade loaded successfully")

except :
    print("no previous data found ")

with open("trade_log.csv","a",newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Stock","Type","Entry","Exit","Stoploss","Takeprofit","Profit"])

while True:
    print("---------MENU------------")
    print("1.place trade")
    print("2.trade history")
    print("3.exit")

    choice = input("enter your choice:  ")

    if choice == '1':
        price = random.randint(int(support-10),int(resistance + 10))
        prices.append(price)

        print("recent price is : ",price )

        if price <= support + 2:
            trade_type = "BUY"
            print("BUY SIGNAL ")

        elif price >= resistance - 2:
            trade_type = "SELL"
            print("SELL SIGNAL ")

        else :
            trade_type = "WAIT"
            print("WAIT TRADE IN SIDE WISE ")

        stock = input("enter the stock name : ")
        entry = float(input("enter the entry price : "))
        exit_price = float(input("enter the exit price : "))
        stoploss = float(input("enter the stoploss : "))
        take_profit = float(input("enter the take profit : "))

        if exit_price >= take_profit :
            print("TARGET HITS ! ")
            profit = take_profit - entry

        elif exit_price <= stoploss:
            print("STOPLOSS HIT ")
            profit = stoploss - entry

        else:
            profit = exit_price - entry

        trade = {
            "name":stock,
            "trade_type":trade_type,
            "entry":entry,
            "exit_price":exit_price,
            "stoploss":stoploss,
            "take_profit":take_profit,
            "profit":profit
            }
        trades.append(trade)
        with open("trade_log.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                stock,
                trade_type,
                entry,
                exit_price,
                stoploss,
                take_profit,
                profit
                ])
        print("trade saved ")

    elif choice == '2':
        print("trade history")
        if len(trades) == 0:
            print("no trades yet ")
        for t in trades:
            print("stock",t["name"])
            print("trade_type",t["trade_type"])
            print("entry",t["entry"])
            print("exit",t["exit_price"])
            print("stoploss",t["stoploss"])
            print("takeprofit",t["take_profit"])
            print("profit",t["profit"])
        total_profit = 0
        wins = 0
        losses = 0
        for t in trades:
            total_profit += t["profit"]

            if t["profit"] > 0:
                wins += 1

            else :
                losses += 1
        total_trades = len(trades)
        if total_trades > 0:
            win_rate = (wins/total_trades)*100

        else :
            win_rate = 0
        print("--------ANALYSIS---------")
        print("total trades : " , total_trades)
        print("winning trades : ",wins)
        print("losing trades : ",losses)
        print("win rate :",round(win_rate,2),"%")
        print("total profit : ",total_profit)
        

    elif choice == '3':
        print("exit from the platform ")
        break
    else:
        print("invalid input ! ")

    print("recent prices : ",prices[-5:])
    print("-------------------------------")

    time.sleep(2)
        
            
