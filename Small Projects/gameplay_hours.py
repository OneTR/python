import math

while True:
    try:
        played_Hours = float(input("Enter your played hours: "))
        break
    except ValueError:
        print("Please enter only numbers.")
        continue

played_Days = played_Hours // 24
played_Hour_Amount = played_Hours % 24
played_Mins = played_Hour_Amount * 60
played_Min_Count = played_Mins % 60

print(int(played_Days), int(played_Hour_Amount), round(played_Min_Count))

while True:
    try:
        played_separate_Days = int(input("Enter your played days: "))
        played_separate_Hours = int(input("Enter your played hours: "))
        played_separate_Mins = int(input("Enter your played minutes: "))
        break
    except ValueError:
        print("Please enter only numbers.")
        continue

played_total_Hours = played_separate_Days * 24 + played_separate_Hours + played_separate_Mins / 60

print(float(played_total_Hours))