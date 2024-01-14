puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

excursion_price = float(input())
p = int(input())
d = int(input())
b = int(input())
m = int(input())
t = int(input())

earnings = puzzle * p + doll * d + bear * b + minion * m + truck * t
total_toys = p + d + b + m + t
if total_toys >= 50:
    discount = earnings * 0.25
else:
    discount = 0
total_earnings = earnings - discount
rent = total_earnings * 0.10
total_earnings -= rent
if total_earnings >= excursion_price:
    money_left = total_earnings - excursion_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = excursion_price - total_earnings
    print(f"Not enough money! {money_needed:.2f} lv needed.")