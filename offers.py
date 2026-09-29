# offers.py


def display_offers(subtotal, combo_order):
    cold_coffee = False
    gift = False

    # Cold coffee offer for ₹500–₹1500
    if 500 <= subtotal <= 1500:
        cold_coffee = True

    # Combo customer gets a gift
    if combo_order == "yes":
        gift = True

    print("\nSPECIAL OFFERS")

    if cold_coffee:
        print("✓ Congratulations! You get a FREE Cold Coffee!")

    if gift:
        print("✓ Combo Offer: You receive a FREE GIFT!")

    if not cold_coffee and not gift:
        print("No complimentary offers on this order.")