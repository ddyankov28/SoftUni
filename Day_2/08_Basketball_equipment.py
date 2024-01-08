annual_tax = int(input())

shoes = annual_tax - (annual_tax * 0.4)
shirt = shoes - (shoes * 0.2)
ball = (1 / 4) * shirt
accessories = (1 / 5) * ball

print(annual_tax + shoes + shirt + ball + accessories)