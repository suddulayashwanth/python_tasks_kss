import pandas as pd

prices = {"Pen": 10, "Book": 50, "Pencil": 5, "Bag": 500}

cart = []

try:
    number_of_items = int(input("Enter number of items: "))

    for i in range(number_of_items):
        item = input("Enter item name: ").title()

        if item in prices:
            cart.append(item)
        else:
            print(item, "is not available")

    cart_data = pd.DataFrame({"Item": cart})

    cart_data["Price"] = cart_data["Item"].map(prices)

    unique_items = set(cart_data["Item"])

    total_cost = cart_data["Price"].sum()

    print("Shopping cart:")

    print(cart_data)

    print("Unique items:", unique_items)

    print("Total cost:", total_cost)

except ValueError:
    print("Invalid input! Enter a number.")