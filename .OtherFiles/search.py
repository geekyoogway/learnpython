import pandas as pd
import yfinance as yf
import mplfinance as mpf

def generate_signals(data):
    signals = []
    for i in range(1, len(data)):
        if data['TEMA1'].iloc[i] > data['Close'].iloc[i] and data['TEMA1'].iloc[i-1] <= data['Close'].iloc[i-1]:
            signals.append(('Buy', data.index[i], data['Low'].iloc[i]))
        elif data['TEMA1'].iloc[i] < data['Close'].iloc[i] and data['TEMA1'].iloc[i-1] >= data['Close'].iloc[i-1]:
            signals.append(('Sell', data.index[i], data['High'].iloc[i]))
        else:
            signals.append('')
    signals.append('')
    return signals

if __name__ == "__main__":
    # Ticker symbol for the stock (e.g., Nifty 50)
    ticker = "^NSEI"

    # Fetch historical data for the stock from Yahoo Finance
    stock_data = yf.download(ticker, start="2023-01-01", end="2023-08-05", interval="1d")

    # Calculate three TEMA using pandas' rolling() function
    stock_data['TEMA1'] = stock_data['Close'].ewm(span=20, adjust=False).mean().ewm(span=20, adjust=False).mean().ewm(span=20, adjust=False).mean()
    stock_data['TEMA2'] = stock_data['Close'].ewm(span=30, adjust=False).mean().ewm(span=30, adjust=False).mean().ewm(span=30, adjust=False).mean()
    stock_data['TEMA3'] = stock_data['Close'].ewm(span=40, adjust=False).mean().ewm(span=40, adjust=False).mean().ewm(span=40, adjust=False).mean()

    # Generate buy and sell signals based on TEMA1
    signals = generate_signals(stock_data)

    # Create the addplot list with three TEMA lines and buy/sell signals
    apds = [
        mpf.make_addplot(stock_data['TEMA1'], color='orange'),
        mpf.make_addplot(stock_data['TEMA2'], color='blue'),
        mpf.make_addplot(stock_data['TEMA3'], color='green'),
        mpf.make_addplot([], scatter=signals, markersize=100, marker='^', color='g')
    ]

    # Plot the candlestick chart with TEMA and signals using mplfinance
    mpf.plot(stock_data, type='candle', style='yahoo', title=f'{ticker} Candlestick Chart with TEMA and Buy/Sell Signals',
             ylabel='Price', volume=True, addplot=apds)
