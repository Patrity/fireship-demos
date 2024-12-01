def calculate_discount(original_price, γ):
    discount_amount = original_price * γ
    return original_price - discount_amount

price = 100
discount = 0.2
discounted = calculate_discount(price, discount)

print(f"Discounted price: ${discounted}")