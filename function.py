from config import API_KEY
from plyer import notification

import requests

BASE_URL = "https://www.alphavantage.co/query"

# Function to get stock price
def get_stock_price(symbol):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": API_KEY,
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        # Parse the most recent stock price
        latest_time = list(data["Time Series (1min)"].keys())[0]
        price = float(data["Time Series (1min)"][latest_time]["1. open"])
        return price
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None
    
# Function to read stocks.txt
def read_file(filename):
    # Dictionary to store stock and limit tuple pairs
    stocks = {}

    # Open file in 'read' mode
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                stock_name = parts[0]
                lower_limit = parts[1]
                upper_limit = parts[2]
                stocks[stock_name] = (lower_limit, upper_limit)
    
    return stocks

# Send macOS notification 
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Stock Tracker',
        timeout=10  # Duration in seconds
    )