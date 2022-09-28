print("Welcome to the City Park!\n")

height = int(input("What is your height in cm? "))
price = 0


if height >= 120:
    age = int(input("How old are you? "))

    if 18 <= age < 45:
        price = 12
        print(f"Adult tickets are ${price}.")
    elif 12 <= age < 18:
        price = 7
        print(f"Youth tickets are ${price}.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        price = 5
        print(f"Children tickets are ${price}.")

    wants_photo = input("Do you want photos? Y or N ")

    answer = wants_photo.lower()

    if answer == "y":
        price += 3
        print(f"You have to pay ${price}.")
    elif answer == "n":
        print(f"You have to pay ${price}.")
else:
    print("Sorry, you have to grow taller before you can ride.")