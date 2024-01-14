n = int(input())

if n <= 100:
    bonus = 5
elif n > 100 and n <= 1000:
    bonus = n * 0.20
else:
    bonus = n * 0.10

if n % 2 == 0:
    extra_bonus = 1
elif n % 10 == 5:
    extra_bonus = 2
else:
    extra_bonus = 0

print(bonus + extra_bonus)
print(n + bonus + extra_bonus)