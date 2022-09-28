print("Welcome to the Freddy Fazbear's Pizzeria!\nSmall Pizzas: $15\nMedium Pizzas: $20\nLarge Pizzas: $25\nAdd pepperoni to small pizzas: +$2\nAdd pepperoni to medium and large pizzas: +$3\nExtra cheese for any size pizza: +$1\n")

size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Would you like to have pepperoni? Y or N ")
cheese = input("Would you like to have extra cheese? Y or N ")
bill = 0

size_lower = size.lower()
add_pepperoni = pepperoni.lower()
extra_cheese = cheese.lower()

if size_lower == "s":
    bill = 15
    if add_pepperoni == "y":
            bill += 2
elif size_lower == "m":
    bill = 20
    if add_pepperoni == "y":
            bill += 3
elif size_lower == "l":
    bill = 25
    if add_pepperoni == "y":
            bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")