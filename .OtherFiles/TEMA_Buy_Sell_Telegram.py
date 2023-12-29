import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
from telegram import Bot
from telegram import Update
import requests



def download_nifty_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date, interval='15m')
    return data

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



def send_message(text):
    try:
        token = '6665994599:AAGBibkGvqVuGWy5X1w_TiMfJtmVFZAmkAQ'
        chat_id = 918897689


        request_url = f"https://api.telegram.org/bot{token}/sendMessage"
        request_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"

        results = requests.get(request_url)
        print(results.json())
    except:
        print("Error")



if __name__ == "__main__":
    try:
        ########### Telegram BOT ##################

        ticker = "^NSEI"  # Ticker symbol for Nifty index
        start_date = "2023-07-01"  # Start date in YYYY-MM-DD format
        end_date = "2023-08-09"    # End date in YYYY-MM-DD format
        df = download_nifty_data(ticker, start_date, end_date)
        window = 14

        

        


    # Calculate Triple EMA
        df['TEMA5'] = ta.tema(df['Close'], length=5)
        df['TEMA10'] = ta.tema(df['Close'], length=10)
        df['TEMA20'] = ta.tema(df['Close'], length=20)
        df['RSI'] = calculate_rsi(df['Close'], window)


        df['Buy_Signal'] = (df['TEMA5'] > df['TEMA10']) & (df['TEMA10'] > df['TEMA20']) & (df['RSI']>70)
        df['Sell_Signal'] = (df['TEMA5'] < df['TEMA10']) & (df['TEMA10'] < df['TEMA20']) & (df['RSI']<30)
        # df['Buy_Signal'] = (df['TEMA5'] > df['TEMA10']) & (df['TEMA5'] > df['TEMA20']) & (df['TEMA10'] > df['TEMA20'])
        # df['Sell_Signal'] = (df['TEMA20'] > df['TEMA5']) & (df['TEMA20'] > df['TEMA10']) & (df['TEMA10'] > df['TEMA5'])
        # print(df)

        # print(df['Buy_Signal']==True)
        for index, row in df.iterrows():
            if row['Buy_Signal'] == True:
                time = index.strftime('%Y-%m-%d %H:%M:%S')
                # time = time.split(' ')[1]
                data_dict = row.to_dict()
                close = data_dict.get('Close')
                close = round(close / 50) * 50

                text = f"<----Buy_Signal----> \n Date Time - {time} \n BUY NIFTY CE -{close}"
                print(text)
            
            if row['Sell_Signal'] == True:
                time = index.strftime('%Y-%m-%d %H:%M:%S')
                # time = time.split(' ')[1]
                data_dict = row.to_dict()
                close = data_dict.get('Close')
                close = round(close / 50) * 50

                text = f"<----Sell_Signal----> \n Date Time - {time} \n BUY NIFTY PE -{close}"
                print(text)
        

        # print(df)
        # df.to_csv("C:\\Users\\rames\\Downloads\\ezyzip\\Results\\results.csv")
        

        # ------------TELEGRAM MESSAGE --------------------#
        # for index, row in df.iterrows():
        #     if row['Buy_Signal'] == True:

        #         time = index.strftime('%Y-%m-%d %H:%M:%S')
        #         time = time.split(' ')[1]
        #         data_dict = row.to_dict()
        #         close = data_dict.get('Close')
        #         close = round(close / 50) * 50

        #         text = f"<----Buy_Signal----> \n Date Time - {time} \n BUY NIFTY CE -{close}"
        #         send_message(text)
            
        #     if row['Sell_Signal'] == True:
        #         time = index.strftime('%Y-%m-%d %H:%M:%S')
        #         time = time.split(' ')[1]
        #         data_dict = row.to_dict()
        #         close = data_dict.get('Close')
        #         close = round(close / 50) * 50

        #         text = f"<----Sell_Signal----> \n Date Time - {time} \n BUY NIFTY PE -{close}"
        #         send_message(text)
        
        # ------------TELEGRAM MESSAGE --------------------#

        #--------------------PLOT--------------------------#
        # # Plot the signals and TEMA values
        # plt.figure(figsize=(12, 6))
        # plt.plot(df.index, df['Close'], label='Close Price', color='blue')
        # plt.plot(df.index, df['TEMA5'], label='TEMA(5)', color='orange')
        # plt.plot(df.index, df['TEMA10'], label='TEMA(10)', color='green')
        # plt.plot(df.index, df['TEMA20'], label='TEMA(20)', color='red')
        # plt.plot(df[df['Buy_Signal']].index, df[df['Buy_Signal']]['TEMA5'], '^', markersize=10, color='green', label='Buy Signal', alpha=1)
        # plt.plot(df[df['Sell_Signal']].index, df[df['Sell_Signal']]['TEMA5'], 'v', markersize=10, color='red', label='Sell Signal', alpha=1)
        # plt.title('Triple EMA Crossover Trading Strategy')
        # plt.xlabel('Date')
        # plt.ylabel('Price')
        # plt.legend()
        # plt.show()
    except:
        print("Error")
