price_per_kg_veg = float(input())
price_per_kg_fruit = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

win_in_leva = price_per_kg_veg * total_kg_veg + price_per_kg_fruit * total_kg_fruit
win_in_euro = win_in_leva / 1.94
print(format(win_in_euro, '.2f'))