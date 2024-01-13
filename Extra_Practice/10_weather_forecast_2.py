grad = float(input())
if grad >= 5 and grad <= 11.9:
    print("Cold")
elif grad >= 12 and grad <= 14.9:
    print("Cool")
elif grad >= 15 and grad <= 20:
    print("Mild")
elif grad >= 20.1 and grad <= 25.9:
    print("Warm")
elif grad >= 26 and grad <= 35:
    print("Hot")
else:
    print("unknown")