w_in_meters = float(input())
h_in_meters = float(input())

rows = int(w_in_meters / 1.2)
columns = int((h_in_meters - 1) / 0.7)
print(rows * columns - 3)