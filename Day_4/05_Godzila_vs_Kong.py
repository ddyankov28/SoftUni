budget = float(input())
actors = int(input())
clothes_price = float(input())

decor = budget * 0.10
if actors > 150:
    clothes_discount = (clothes_price * actors) * 0.10
else:
    clothes_discount = 0

total_cost = decor + ((clothes_price * actors) - clothes_discount)
if total_cost > budget:
    money_needed = total_cost - budget
    print(f"Not enough money!\nWingard needs {money_needed:.2f} leva more.")
else:
    money_left = budget - total_cost
    print(f"Action!\nWingard starts filming with {money_left:.2f} leva left.")
