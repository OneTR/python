weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / height ** 2
bmi_rounded = round(bmi)

if bmi_rounded < 18.5:
    print(f"Your BMI is: {bmi_rounded}\nYou are underweight. You should gain more weight.")
elif 18.5 <= bmi_rounded < 25:
    print(f"Your BMI is: {bmi_rounded}\nYou have a normal weight.")
elif 25 <= bmi_rounded < 30:
    print(f"Your BMI is: {bmi_rounded}\nYou are overweight. You should lose some weight.")
elif 30 <= bmi_rounded < 35:
    print(f"Your BMI is: {bmi_rounded}\nYou are obese. You should have a proper diet for losing weight.")
elif bmi_rounded >= 35:
    print(f"Your BMI is: {bmi_rounded}\nYou are clinically obese. You should seek medical treatment.")