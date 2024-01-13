green_paint = 3.4
red_paint = 4.3
x = float(input())
s_door = 1.2 * 2
y = float(input())
s_windows = 2 * (1.5 * 1.5)
h = float(input())

s_green = 2 * (x * x) - s_door - s_windows + 2 * (x * y)
green_liters = format(s_green / green_paint, ".2f")
s_red = 2 * ((x * h) / 2) + 2 * (x * y)
red_liters = format(s_red / red_paint, ".2f")
print(green_liters)
print(red_liters)
