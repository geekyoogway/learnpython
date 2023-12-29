import pandas as pd
import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

def generate_signals(data):
    signals = []
    for i in range(1, len(data)):
        if data['TEMA_5'].iloc[i] > data['Close'].iloc[i] and data['TEMA_5'].iloc[i-1] <= data['Close'].iloc[i-1]:
            signals.append(('Buy', data.index[i]))
        elif data['TEMA_5'].iloc[i] < data['Close'].iloc[i] and data['TEMA_5'].iloc[i-1] >= data['Close'].iloc[i-1]:
            signals.append(('Sell', data.index[i]))
        else:
            signals.append(('Hold', data.index[i]))
    return signals

if __name__ == "__main__":
    # Ticker symbol for the stock (e.g., Nifty 50)
    ticker = "^NSEI"

    # Fetch historical data for the stock from Yahoo Finance
    stock_data = yf.download(ticker, start="2023-08-06", end="2023-08-06", interval="15min")

    # Calculate three TEMA using pandas' rolling() function
    stock_data['TEMA_5'] = stock_data['Close'].ewm(span=5, adjust=False).mean().ewm(span=5, adjust=False).mean().ewm(span=5, adjust=False).mean()
    stock_data['TEMA_10'] = stock_data['Close'].ewm(span=10, adjust=False).mean().ewm(span=10, adjust=False).mean().ewm(span=10, adjust=False).mean()
    stock_data['TEMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean().ewm(span=20, adjust=False).mean().ewm(span=20, adjust=False).mean()

    # Generate buy and sell signals based on TEMA
    signals = generate_signals(stock_data)

    # Plot the candlestick chart with TEMA using mplfinance
    apds = [mpf.make_addplot(stock_data['TEMA_5'], color='orange', panel='lower'),
            mpf.make_addplot(stock_data['TEMA_10'], color='purple', panel='lower'),
            mpf.make_addplot(stock_data['TEMA_20'], color='blue', panel='lower')]

    # Create a scatter plot for buy/sell signals using matplotlib
    for signal, date in signals:
        if signal == 'Buy':
            plt.scatter(date, stock_data.loc[date, 'Low'], marker='^', color='g', s=100, label='Buy Signal')
        elif signal == 'Sell':
            plt.scatter(date, stock_data.loc[date, 'High'], marker='v', color='r', s=100, label='Sell Signal')

    # plt.legend()

    # Display the candlestick chart with TEMA and buy/sell signals
    mpf.plot(stock_data, type='candle', style='yahoo', title=f'{ticker} Candlestick Chart with TEMA',
             ylabel='Price', volume=True, addplot=apds)

    # plt.show()
