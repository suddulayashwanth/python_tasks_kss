prices = [100, 200, 300, 400]

updated_prices = [
    price * 0.90 if price > 200 else price
    for price in prices
]

print("Original prices:", prices)
print("Updated prices:", updated_prices)