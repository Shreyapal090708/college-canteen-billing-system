# menu.py

MENU = {
    1: ("Burger", 80),
    2: ("Pizza", 120),
    3: ("Sandwich", 70),
    4: ("Momos", 60),
    5: ("French Fries", 90),
    6: ("Cold Drink", 40),
    7: ("Coffee", 50),
    8: ("Combo Meal", 200)
}


def display_menu():
    print("\nMENU")
    print("-" * 45)

    for number, (item, price) in MENU.items():
        print(f"{number}. {item:<20} ₹{price}")

    print("-" * 45)