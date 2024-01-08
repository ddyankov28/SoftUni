orders_chicken = int(input())
orders_fish = int(input())
orders_vegan = int(input())

chicken = 10.35
fish = 12.40
vegan = 8.15
delivery = 2.50

price = chicken * orders_chicken + fish * orders_fish + vegan * orders_vegan
desert = price * 0.2
total_price = price + desert + delivery
print(total_price)
