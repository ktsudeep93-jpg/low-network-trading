import time
import random

print("LOW NETWORK TRADING PLATFORM ")

support = float(input("please enter the value at support zone : "))
resistance = float(input("please enter the value at resistance zone : "))

prices = []

while True :
    price = random.randint(int(support-10),int(resistance+10))
    prices.append(price)

    print("current price is : ", price )

    if price > resistance :
        print("BUY SIGNAL ")

    elif price < support :
        print("SELL SIGNAL ")

    else:
        print("WAIT: MARKET MOVING IN SIDEWAYS ")

    print("recent prices ",prices[-5:])
    print("------------------------------/n")

    time.sleep(2)
