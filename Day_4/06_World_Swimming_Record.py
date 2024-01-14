wr_in_secs = float(input())
distance = float(input())
seconds_per_meter = float(input())

ivan_pace = distance * seconds_per_meter
ivan_pace += (distance // 15) * 12.5
if ivan_pace >= wr_in_secs:
    time = ivan_pace - wr_in_secs
    print(f"No, he failed! He was {time:.2f} seconds slower.")
else:
    time = wr_in_secs - ivan_pace
    print(f"Yes, he succeeded! The new world record is {ivan_pace:.2f} seconds.")