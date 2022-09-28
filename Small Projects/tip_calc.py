print("Welcome to the Tip Calculator!\n")

bill = float(input("What was the total bill? ₺"))
people_Count = int(input("How many people to split the bill? "))
tip_Percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
price_Per_Person = 0
total_Price = 0

if tip_Percent == 10 or tip_Percent == 12 or tip_Percent == 15:
    total_Price = bill * (tip_Percent / 100) + bill
    price_Per_Person = total_Price / people_Count
    print("Each person should pay: ₺" + "{:.2f}".format(price_Per_Person))
else:
    print("You should enter the percentage as the three given options.")