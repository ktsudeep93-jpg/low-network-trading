import csv
from datetime import datetime

trades = []

support = float(input("Enter the support zone price: "))
resistance = float(input("Enter the resistance zone price: "))

prices = []

while True:
    print("\n------ MENU ------")
    print("1. place trade")
    print("2. trade history")
    print("3. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter current price: "))
        prices.append(price)

        print("recent prices:", prices)

        # Signal logic
        if price <= support:
            trade_type = "BUY"
            print("BUY SIGNAL")
        elif price >= resistance:
            trade_type = "SELL"
            print("SELL SIGNAL")
        else:
            trade_type = "WAIT"
            print("WAIT - market sideways")

        print("suggested trade type:", trade_type)

        stock = input("Enter stock name: ")
        entry = float(input("Enter entry price: "))
        exit_price = float(input("Enter exit price: "))
        stoploss = float(input("Enter stoploss: "))
        take_profit = float(input("Enter take profit: "))

        # Profit logic
        if trade_type == "BUY":
            profit = exit_price - entry
        elif trade_type == "SELL":
            profit = entry - exit_price
        else:
            profit = 0

        # Time
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Trade dictionary
        trade = {
            "name": stock,
            "trade_type": trade_type,
            "entry": entry,
            "exit_price": exit_price,
            "stoploss": stoploss,
            "take_profit": take_profit,
            "profit": profit,
            "time": time
        }

        trades.append(trade)

        # Save to CSV
        with open("trade_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                stock,
                trade_type,
                entry,
                exit_price,
                stoploss,
                take_profit,
                profit,
                time
            ])

        print("trade saved to CSV!")

    elif choice == "2":
        print("\n------ TRADE HISTORY ------")

        if len(trades) == 0:
            print("No trades yet")

        total_profit = 0
        win = 0
        loss = 0

        for t in trades:
            print("--------------------------")
            print("Stock:", t["name"])
            print("Type:", t["trade_type"])
            print("Entry:", t["entry"])
            print("Exit:", t["exit_price"])
            print("Stoploss:", t["stoploss"])
            print("Take Profit:", t["take_profit"])
            print("Profit:", t["profit"])
            print("Time:", t["time"])

            total_profit += t["profit"]

            if t["profit"] > 0:
                win += 1
            elif t["profit"] < 0:
                loss += 1

        total_trades = len(trades)

        print("\n------ ANALYSIS ------")
        print("Total trades:", total_trades)
        print("Total profit:", total_profit)
        print("Winning trades:", win)
        print("Losing trades:", loss)

        if total_trades > 0:
            win_rate = (win / total_trades) * 100
            print("Win rate:", round(win_rate, 2), "%")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid input!")
