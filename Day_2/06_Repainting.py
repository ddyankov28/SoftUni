nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

total_paint = paint + 0.1 * paint
total_nylon = nylon + 2
bags = 0.40

consumables_price = total_nylon * nylon_price + total_paint * paint_price + thinner * thinner_price + bags
workers_salary = 0.3 * consumables_price
print (consumables_price + workers_salary * hours)

