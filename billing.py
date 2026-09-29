# billing.py


def calculate_bill(subtotal, peak_hours, combo_order):
    discount_10 = 0
    peak_discount = 0
    voucher_discount = 0

    # 10% discount if bill is greater than ₹500
    if subtotal > 500:
        discount_10 = subtotal * 0.10

    # Additional 3% discount during peak college hours
    if peak_hours == "yes":
        peak_discount = subtotal * 0.03

    # Combo voucher discount
    if combo_order == "yes":
        voucher_discount = 50

    total_discount = discount_10 + peak_discount + voucher_discount
    final_amount = subtotal - total_discount

    if final_amount < 0:
        final_amount = 0

    return discount_10, peak_discount, voucher_discount, final_amount


def print_bill(cart, subtotal, discount_10,
               peak_discount, voucher_discount, final_amount):

    print("\n")
    print("=" * 45)
    print("             FINAL BILL")
    print("=" * 45)

    for item_name, quantity, item_total in cart:
        print(f"{item_name:<20} x {quantity:<3} ₹{item_total}")

    print("-" * 45)
    print(f"Subtotal:                         ₹{subtotal:.2f}")

    if discount_10 > 0:
        print(f"10% Discount:                    -₹{discount_10:.2f}")

    if peak_discount > 0:
        print(f"Peak Hour Discount (3%):        -₹{peak_discount:.2f}")

    if voucher_discount > 0:
        print(f"Combo Voucher Discount:          -₹{voucher_discount:.2f}")

    print("-" * 45)
    print(f"FINAL AMOUNT:                     ₹{final_amount:.2f}")
    print("=" * 45)