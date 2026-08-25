stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")
print("Available stocks:", stock_prices)

while True:
    stock_name = input("Enter stock name (or type done): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock_name] = quantity
        value = stock_prices[stock_name] * quantity
        total_value += value

        print(stock_name, "value is $", value)
    else:
        print("Stock not available. Please choose from the list.")

print("\nYour Portfolio:")

for stock, quantity in portfolio.items():
    print(stock, "-", quantity, "shares")

print("Total Portfolio Value: $", total_value)