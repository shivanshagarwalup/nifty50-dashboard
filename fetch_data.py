import yfinance as yf
import json
import os
from datetime import datetime, timedelta

def fetch_nifty_data():
    print("Fetching Nifty 50 Data (^NSEI) from Yahoo Finance...")
    
    # Nifty 50 ticker symbol on Yahoo Finance
    ticker = "^NSEI"
    
    # 20 years from today
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * 20)
    
    # Download data
    data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    if data.empty:
        print("Failed to fetch data or no data available for the given range.")
        return

    # Extract closing prices and format them into the required JSON structure
    formatted_data = []
    
    # yfinance returns a MultiIndex column DataFrame now in some versions, or single index.
    # Safe extraction of Close price:
    if 'Close' in data.columns:
        close_prices = data['Close']
        if isinstance(close_prices, type(data)): # It's a dataframe (MultiIndex possible)
            close_prices = close_prices.iloc[:, 0]
    else:
        print("Close column not found. Available columns:", data.columns)
        return

    # Drop null values (holidays/weekends)
    close_prices = close_prices.dropna()

    for date, price in close_prices.items():
        formatted_data.append({
            "x": date.strftime('%Y-%m-%d'),
            "y": round(float(price), 2)
        })

    # Save to file
    output_file = 'nifty50_data.json'
    with open(output_file, 'w') as f:
        json.dump(formatted_data, f)
        
    print(f"Successfully saved {len(formatted_data)} daily records to {output_file}.")

if __name__ == "__main__":
    fetch_nifty_data()
