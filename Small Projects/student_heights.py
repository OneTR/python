student_heights = input("Please enter student heights in cm.\n").split(" ")
height_sum = 0
num_students = 0

for height in student_heights:
    height_sum += int(height)
    num_students += 1

avg_height = round(height_sum / num_students)

print(f"The average height of students is: {avg_height} cm.")