budget = float(input())
N = int(input())
M = int(input())
P = int(input())
N_price = 250 * N
M_price = N_price * 0.35 * M
P_price = N_price * 0.10 * P
discount = 0
total_price = N_price + M_price + P_price
if N > M:
    discount = total_price * 0.15
total_price -= discount
if total_price > budget:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
else:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")