import random
import os

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

if choice == 0:
    print(f"Your choice:{rock}")
elif choice == 1:
    print(f"Your choice:{paper}")
elif choice == 2:
    print(f"Your choice:{scissors}")

comp_choice = random.randint(0, 2)

if comp_choice == 0:
    print(f"\nComputer chose:{rock}")
elif comp_choice == 1:
    print(f"\nComputer chose:{paper}")
elif comp_choice == 2:
    print(f"\nComputer chose:{scissors}")

if choice == comp_choice:
    print("\nYou tied.")
elif choice == 0 and comp_choice == 1:
    print("\nYou lose.")
elif choice == 0 and comp_choice == 2:
    print("\nYou win.")
elif choice == 1 and comp_choice == 0:
    print("\nYou win.")
elif choice == 1 and comp_choice == 2:
    print("\nYou lose.")
elif choice == 2 and comp_choice == 0:
    print("\nYou lose.")
elif choice == 2 and comp_choice == 1:
    print("\nYou win.")
os.system("pause")