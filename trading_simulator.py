import random
from datetime import datetime, timedelta

def generate_fake_data(days=30):
    price = 100.0
    data = []
    start_date = datetime.now() - timedelta(days=days)
    for i in range(days):
        date = (start_date + timedelta(days=i+1)).strftime("%Y-%m-%d")
        change = random.uniform(-1, 1)  # price change between -1 and 1
        price = round(price + change, 2)
        if change > 0.5:
            signal = "Buy"
        elif change < -0.5:
            signal = "Sell"
        else:
            signal = "Hold"
        data.append((date, price, signal))
    return data

def main():
    print("Educational Algorithmic Trading Bot Simulator on Past Data\n")
    data = generate_fake_data(30)
    print(f"{'Date':<12} {'Price':<8} {'Signal':<6}")
    print("-" * 30)
    for row in data:
        print(f"{row[0]:<12} ${row[1]:<7} {row[2]}")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")  # Keeps the window open until Enter is pressed
