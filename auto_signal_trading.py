import random
import time

print("LOW NETWORK TRADING SIMULATOR")

support = float(input("Enter support price: "))
resistance = float(input("Enter resistance price: "))

prices = []
trades = []

while True:

    print("\n===== MENU =====")
    print("1 Place Trade")
    print("2 View Trade History")
    print("3 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        price = random.randint(int(support - 10), int(resistance + 10))
        prices.append(price)

        print("\nCurrent price:", price)

        if price <= support + 2:
            print("AUTO SIGNAL: BUY (near support)")
            trade_type = "BUY"

        elif price >= resistance - 2:
            print("AUTO SIGNAL: SELL (near resistance)")
            trade_type = "SELL"

        else:
            print("AUTO SIGNAL: WAIT")
            trade_type = "WAIT"

        print("Suggested Trade:", trade_type)

        stock = input("Enter stock name: ")
        entry = float(input("Enter entry price: "))
        exit_price = float(input("Enter exit price: "))
        stoploss = float(input("Enter stoploss price: "))
        take_profit = float(input("Enter take profit price: "))

        if exit_price >= take_profit:
            print("TARGET HIT")
            profit = take_profit - entry

        elif exit_price <= stoploss:
            print("STOPLOSS HIT")
            profit = stoploss - entry

        else:
            profit = exit_price - entry

        trade = {
            "name": stock,
            "type": trade_type,
            "entry": entry,
            "exit_price": exit_price,
            "stoploss": stoploss,
            "take_profit": take_profit,
            "profit": profit
        }

        trades.append(trade)

        file = open("trade_log.txt", "a")
        file.write(stock + " " + trade_type + " " + str(entry) + " " + str(exit_price) + " " + str(profit) + "\n")
        file.close()

        print("Trade saved successfully!")

 
    elif choice == "2":

        print("\nTrade History:")

        if len(trades) == 0:
            print("No trades yet.")

        for t in trades:
            print("-------------------")
            print("Stock:", t["name"])
            print("Type:", t["type"])
            print("Entry:", t["entry"])
            print("Exit:", t["exit_price"])
            print("Stoploss:", t["stoploss"])
            print("Take Profit:", t["take_profit"])
            print("Profit:", t["profit"])

        total_profit = 0
        for t in trades:
            total_profit += t["profit"]

        print("\nTOTAL TRADES:", len(trades))
        print("TOTAL PROFIT:", total_profit)


    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")

    print("\nRecent prices:", prices[-5:])
    print("---------------------------")

    time.sleep(2)
