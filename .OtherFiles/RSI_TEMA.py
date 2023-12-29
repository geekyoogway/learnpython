import yfinance as yf
import pandas as pd
import numpy as np

def calculate_rsi(data, window):
    diff = data.diff(1).dropna()
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    up_chg[diff > 0] = diff[diff > 0]
    down_chg[diff < 0] = diff[diff < 0]
    
    avg_up_chg = up_chg.rolling(window=window).mean()
    avg_down_chg = down_chg.rolling(window=window).mean()
    
    rs = abs(avg_up_chg / avg_down_chg)
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def calculate_tema(data, window):
    ema1 = data.ewm(span=window, adjust=False).mean()
    ema2 = ema1.ewm(span=window, adjust=False).mean()
    ema3 = ema2.ewm(span=window, adjust=False).mean()
    tema = 3 * (ema1 - ema2) + ema3
    
    return tema

# Replace 'AAPL' with the stock symbol you want to analyze
# stock_symbol = 'NSEI'
window = 14  # RSI and TEMA window period

ticker = "^NSEI"  # Ticker symbol for Nifty index
start_date = "2023-08-01"  # Start date in YYYY-MM-DD format
end_date = "2023-08-09"    # End date in YYYY-MM-DD format




# Fetch live data using yfinance
live_data = yf.download(ticker, start=start_date, end=end_date, interval='15m')
 

# Calculate RSI and TEMA
live_data['RSI'] = calculate_rsi(live_data['Close'], window)
live_data['TEMA'] = calculate_tema(live_data['Close'], window)

print(live_data)
