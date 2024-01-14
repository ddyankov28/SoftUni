from math import ceil
series = input()
length = int(input())
pause = int(input())
eat = pause / 8
relax = pause / 4
time_for_looking = pause - eat - relax
if time_for_looking >= length:
    left_time = time_for_looking - length
    print(f"You have enough time to watch {series} and left with {ceil(left_time)} minutes free time.")
else:
    time_needed = length - time_for_looking
    print(f"You don't have enough time to watch {series}, you need {ceil(time_needed)} more minutes.")