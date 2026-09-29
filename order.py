# order.py

from menu import MENU


def take_order():
    cart = []
    subtotal = 0

    while True:
        try:
            choice = int(input("\nEnter item number (0 to finish): "))

            if choice == 0:
                break

            if choice not in MENU:
                print("Invalid item number. Please try again.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            item_name, price = MENU[choice]
            item_total = price * quantity

            cart.append((item_name, quantity, item_total))
            subtotal += item_total

            print(f"{item_name} x {quantity} added to your order.")
            print(f"Item total: ₹{item_total}")

        except ValueError:
            print("Please enter a valid number.")

    return cart, subtotal