student_scores = input("Please enter student scores.\n").split(" ")
highest_score = 0
lowest_score = 100

for score in range(len(student_scores)):
    student_scores[score] = int(student_scores[score])

for highest in student_scores:
    if highest > highest_score:
        highest_score = highest

for lowest in student_scores:
    if lowest < lowest_score:
        lowest_score = lowest

print(f"The highest score in the class is: {highest_score}, the lowest score in the class is: {lowest_score}.")