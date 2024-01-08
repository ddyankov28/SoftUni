pens = 5.80
markers = 7.20
liter = 1.20
num_pens = int(input())
num_markers = int(input())
liters = int(input())
discount = int(input())
total_price = pens * num_pens + markers * num_markers + liter * liters
dis = (discount / 100) * total_price
print(total_price - dis)