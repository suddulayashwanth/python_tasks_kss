product_details = (
    ("Pen", 10, "Stationery"),
    ("Notebook", 50, "Stationery"),
    ("Pencil", 5, "Stationery")
)

products = {
    name: price
    for name, price, category in product_details
}

categories = {
    category
    for name, price, category in product_details
}

cart = []


def display_products():
    print("\nAvailable Products:")

    for name, price in products.items():
        print(f"{name} : {price}")


def find_product(entered_name):
    for product_name in products:
        if product_name.lower() == entered_name.lower():
            return product_name

    raise NameError


def add_to_cart():
    try:
        entered_name = input("Enter product name: ").strip()

        product_name = find_product(entered_name)

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        cart_item = (
            product_name,
            products[product_name],
            quantity
        )

        cart.append(cart_item)

        print("Item added to cart successfully.")

    except ValueError:
        print(
            "Invalid quantity! "
            "Please enter a number greater than zero."
        )

    except NameError:
        print("Product not found in store.")

    except TypeError:
        print("Cart data type error.")


def recursive_bill(items, index=0):
    if index == len(items):
        return 0

    item = items[index]

    if (
        not isinstance(item, tuple)
        or len(item) != 3
        or not isinstance(item[0], str)
        or not isinstance(item[1], (int, float))
        or not isinstance(item[2], int)
    ):
        raise TypeError

    product_price = item[1]
    quantity = item[2]

    current_price = product_price * quantity

    return current_price + recursive_bill(items, index + 1)


def calculate_total_bill():
    try:
        if not cart:
            raise ZeroDivisionError

        total = recursive_bill(cart)

        print("\nItems in Cart:")

        for product_name, price, quantity in cart:
            print(f"{product_name} x {quantity}")

        print("\nTotal Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")


while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        calculate_total_bill()

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please select 1 to 4.")