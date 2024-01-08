length = int(input())
width = int(input())
height = int(input())
no_water_percent = int(input())

size = length * width * height
liters = size / 1000
print(liters - (liters * (no_water_percent / 100)))