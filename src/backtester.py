import random

def get_historical_prices(symbol="bitcoin", days=10):
    # Fake data for demo purposes
    return [random.randint(30000, 60000) for _ in range(days)]

def simple_strategy(prices):
    balance = 1000
    for price in prices:
        if price < sum(prices)/len(prices):  # Buy if below average
            balance += 10
        else:
            balance -= 5
    return balance

if __name__ == "__main__":
    prices = get_historical_prices()
    final_balance = simple_strategy(prices)
    print("Final balance after backtest:", final_balance)
