def calculate_discount(price, discount_percent):
    # Bug: Doesn't check if price is negative or discount > 100
    return price - (price * (discount_percent / 100))
