deposit = float(input())
period_in_months = int(input())
interest_rate = float(input())

result = deposit + period_in_months * (deposit * (interest_rate / 100) / 12)
print(result)