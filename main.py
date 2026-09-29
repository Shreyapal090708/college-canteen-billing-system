# main.py

from menu import display_menu
from order import take_order
from billing import calculate_bill, print_bill
from offers import display_offers


print("=" * 45)
print("       WELCOME TO COLLEGE CANTEEN")
print("=" * 45)

# Display food menu
display_menu()

# Take customer order
cart, subtotal = take_order()

# Check whether an order was placed
if subtotal == 0:
    print("\nNo items were ordered.")
    print("Thank you for visiting the College Canteen!")
    raise SystemExit

# Ask about peak hours
peak_hours = input(
    "\nAre you ordering during peak college hours? (yes/no): "
).strip().lower()

# Ask about combo
combo_order = input(
    "Did you order a combo? (yes/no): "
).strip().lower()

# Calculate bill
discount_10, peak_discount, voucher_discount, final_amount = calculate_bill(
    subtotal,
    peak_hours,
    combo_order
)

# Display final bill
print_bill(
    cart,
    subtotal,
    discount_10,
    peak_discount,
    voucher_discount,
    final_amount
)

# Display special offers
display_offers(subtotal, combo_order)

print("\nThank you for visiting the College Canteen!")
print("Have a great day!")