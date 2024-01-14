hour = int(input())
mins = int(input()) + 15

if mins >= 60:
    hour += 1
    mins = mins % 60
if hour == 24:
    hour = 0
if mins < 10:
    print(f"{hour}:0{mins}")
else:
    print(f"{hour}:{mins}")