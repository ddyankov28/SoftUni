m2_price = 7.61
total_m2 = float(input())
total_price = total_m2 * m2_price
discount = total_price * 0.18
price = total_price - discount
print(f"The final price is: {price} lv.")
print(f"The discount is: {discount} lv.")