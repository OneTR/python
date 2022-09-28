import math

ects_List = []
grade_List = []
credit_Course_List = []
sum_Course = 0
sum_Ects = 0
gpa = 0

while True:
    try:
        course_Count = int(input("Enter your course count: "))
        break
    except ValueError:
        print("Please input integer only.")
        continue

for count in range(course_Count):
    while True:
        try:
            ects_List = ects_List + [int(input("Enter your course ECTS: "))]
            break
        except ValueError:
            print("Please input integer only.")
            continue

for grade in range(course_Count):
    grade_List = grade_List + [input("Enter your letter grade: ")]
    """while True:
        try:
            grade_List = grade_List + [input("Enter your letter grade: ")]
            break
        except""" # Bu kısımda dictionary'deki elemanlar haricinde hiçbir inputu aldırmaman lazım.

grade_Dict = {"A": 4.00, "B1": 3.50, "B2": 3.25, "B3": 3.00, "C1": 2.75, "C2": 2.50, "C3": 2.00, "F1": 1.50, "F4": 0.00} # Harf notlarını hesaplayacak 100 üzerinden kodu da yaz.
grade_List = [grade_Dict[grade] for grade in grade_List]

for avg in range(course_Count):
    credit_Course_List = credit_Course_List + [ects_List[avg] * grade_List[avg]]
    sum_Course = sum_Course + credit_Course_List[avg]
    sum_Ects = sum_Ects + ects_List[avg]

gpa = sum_Course / sum_Ects # CGPA için tekrar düşün.

print("Your GPA is:", gpa)