book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_total = book_pages / pages_per_hour
hours_per_day = hours_total / days
print(int(hours_per_day))