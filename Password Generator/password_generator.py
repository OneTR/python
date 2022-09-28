# EASY LEVEL

import random
password = ""
passList = []
hardPassword = ""

num_letters = int(input("How many letters do you need in your password? "))
num_numbers = int(input("How many numbers do you need in your password? "))
num_symbols = int(input("How many symbols do you need in your password? "))

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters = alphabet.split()
sym = "! # $ % & ( ) * + . , ; : ="
symbols = sym.split()

for letter in range(num_letters):
    valueL = random.randint(1, len(letters) - 1)
    password += letters[valueL]
for num in range(num_numbers):
    valueN = random.randint(1, len(numbers) - 1)
    password += numbers[valueN]
for sym in range(num_symbols):
    valueS = random.randint(1, len(symbols) - 1)
    password += symbols[sym]

print(password)

# HARD LEVEL

for letter in range(num_letters):
    passList.append(random.choice(letters))
for number in range(num_numbers):
    passList.append(random.choice(numbers))
for symbol in range(num_symbols):
    passList.append(random.choice(symbols))

random.shuffle(passList)

for passW in passList:
    hardPassword += passW

print(hardPassword)