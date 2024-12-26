from config import API_KEY
from function import get_stock_price, read_file, send_notification

import time


# Main function
def track_loop():
    stocks = read_file('stocks.txt') # Dictionary of stock symbols and limits

    while True:

        for symbol in stocks.keys():

            price = get_stock_price(symbol)

            if price is not None:

                print(f"{symbol}: ${price}")
                
                if price < float(stocks[symbol][0]):
                    print(f"{symbol} is now ${price}, below threshold of ${stocks[symbol][0]}")
                    send_notification(symbol, f"{symbol} is now ${price}, below threshold of ${stocks[symbol][0]}")
                elif price > float(stocks[symbol][1]):
                    print(f"{symbol} is now ${price}, above threshold of ${stocks[symbol][1]}")
                    send_notification(symbol, f"{symbol} is now ${price}, above threshold of ${stocks[symbol][1]}")
        
        time.sleep(60) # Check every 60 seconds


if __name__ == "__main__":
    track_loop()
