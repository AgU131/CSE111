# Tire Volume Activity
import math
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
print(day_of_week)
print(f"{current_date_and_time:%Y-%m-%d}")
print(current_date_and_time)

print(math.pi)
w = int(input("Enter the width of the tire in mm (ex 205):"))
a = int(input("Enter the aspect ratio of the tire (ex 60):"))
d = int(input("Enter the diameter of the wheel in inches (ex 15):"))
v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")


