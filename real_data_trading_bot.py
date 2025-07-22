# trading_bot.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_data(ticker="BTC-USD", period="20d", interval="1d"):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period=period, interval=interval)
    if data.empty:
        print("No data found. Check ticker or internet connection.")
        return None
    return data

def simulate_strategy(data):
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_10'] = data['Close'].rolling(window=10).mean()
    
    buy_signals = []
    sell_signals = []
    position = False

    for i in range(len(data)):
        if data['SMA_5'].iloc[i] > data['SMA_10'].iloc[i]:
            if not position:
                buy_signals.append(data['Close'].iloc[i])
                sell_signals.append(None)
                position = True
            else:
                buy_signals.append(None)
                sell_signals.append(None)
        elif data['SMA_5'].iloc[i] < data['SMA_10'].iloc[i]:
            if position:
                sell_signals.append(data['Close'].iloc[i])
                buy_signals.append(None)
                position = False
            else:
                buy_signals.append(None)
                sell_signals.append(None)
        else:
            buy_signals.append(None)
            sell_signals.append(None)

    data['Buy'] = buy_signals
    data['Sell'] = sell_signals
    return data

def plot_data(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA_5'], label='SMA 5', color='green')
    plt.plot(data['SMA_10'], label='SMA 10', color='orange')
    plt.scatter(data.index, data['Buy'], label='Buy Signal', marker='^', color='green')
    plt.scatter(data.index, data['Sell'], label='Sell Signal', marker='v', color='red')
    plt.title("Trading Strategy Simulation on Real Data")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    data = get_data()
    if data is not None:
        data = simulate_strategy(data)
        plot_data(data)

if __name__ == "__main__":
    main()
