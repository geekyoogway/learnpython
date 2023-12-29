import pandas as pd
import mplfinance as mpf
import yfinance as yf
import pandas_ta as ta


def download_nifty_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date, interval='15m')
    return data

if __name__ == "__main__":

    # ticker = "^NSEI"  # Ticker symbol for Nifty index
    # start_date = "2023-08-03"  # Start date in YYYY-MM-DD format
    # end_date = "2023-08-06"    # End date in YYYY-MM-DD format

    # data = download_nifty_data(ticker, start_date, end_date)
    # print(data)
    # data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
    # data.set_index('Date', inplace=True)
    # Assuming you have historical data in a CSV file with 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume' columns
    # data = pd.read_csv('historical_data.csv')
    # data['Date'] = pd.to_datetime(data['Date'])

    data = pd.read_csv("C:\\Users\\rames\\Downloads\\ezyzip\\data.csv")
    # data.set_index('Date', inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])

    # Now the 'Date' column is a DatetimeIndex, and you can perform datetime-related operations
    # For example, you can access the year, month, or day of each date
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    data['Day'] = data['Date'].dt.day
    data.set_index('Date', inplace=True)



    # Resample data to 15-minute time frame
    data_15min = data.resample('15T').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })

    # Plot candlestick chart
    # mpf.plot(data_15min, type='candle', style='yahoo', title='15-Minute Candlestick Chart')
    data['TEMA5'] = ta.tema(data['Close'], length=5)
    data['TEMA10'] = ta.tema(data['Close'], length=10)
    data['TEMA20'] = ta.tema(data['Close'], length=20)

    # Generate trading signals
    data['Buy_Signal'] = (data['TEMA5'] > data['TEMA10']) & (data['TEMA10'] > data['TEMA20'])
    data['Sell_Signal'] = (data['TEMA5'] < data['TEMA10']) & (data['TEMA10'] < data['TEMA20'])

    # Plot the signals and TEMA values
    mpf.figure(figsize=(12, 6))
    mpf.plot(data.index, data['Close'], label='Close Price', color='blue')
    mpf.plot(data.index, data['TEMA5'], label='TEMA(5)', color='orange')
    mpf.plot(data.index, data['TEMA10'], label='TEMA(10)', color='green')
    mpf.plot(data.index, data['TEMA20'], label='TEMA(20)', color='red')
    mpf.plot(data[data['Buy_Signal']].index, data[data['Buy_Signal']]['TEMA5'], '^', markersize=10, color='green', label='Buy Signal', alpha=1)
    mpf.plot(data[data['Sell_Signal']].index, data[data['Sell_Signal']]['TEMA5'], 'v', markersize=10, color='red', label='Sell Signal', alpha=1)
    mpf.title('Triple EMA Crossover Trading Strategy')
    mpf.xlabel('Date')
    mpf.ylabel('Price')
    mpf.legend()
    mpf.show()
    mpf.plot(data_15min, type='candle', style='yahoo', title='15-Minute Candlestick Chart',addplot=[mpf.make_addplot(data_15min['TEMA'], color='orange', secondary=True)])

    