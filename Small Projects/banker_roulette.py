import random

people = input("Enter the names in the group: ")

roulette = people.split(", ")

paying_person = random.choice(roulette)

print(f"{paying_person} is going to pay the bill today.")