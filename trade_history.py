import random
import time
print("LOW NETWORK TRADING FLATFORM ")

support = float(input("enter the support zone price : "))
resistance = float(input("enter the resistance zone price : "))

prices = []
trades = []

while True :
    price = random.randint(int(support-10),int(resistance+10))
    prices.append(price)

    print("current price ",price)

    if price > resistance :
        print("BUY SIGNAL ")

    elif price < support :
        print("SELL SIGNAL ")

    else :
        print("WAIT-CHART IN SIDEWAYS")

    choice = input("do you want to place an order (yes/no) : ")

    if choice == 'yes':
        stock_name = input("enter the stock name : ")
        entry = float(input("enter the entry price : "))
        exit_price = float(input("enter the exit price : "))

        profit = exit_price - entry

        trade = {
            "name" : stock_name ,
            "entry" : entry,
            "exit_price" : exit_price,
            "profit" : profit
            }
        trades.append(trade)
        print("your order placed ")
        print("saved history ")
        for t in trades:
            print(t)

        print("recent prices : ",prices[-5:])
        print("---------------------------------")

        time.sleep(2)
