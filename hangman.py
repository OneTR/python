import random
import os
from hangman_words import word_list
import hangman_logos

print(hangman_logos.logo)

lives = 9
guess_list = []
blanks_list = []
same_letter_list = []
new_blanks = ""
end_of_game = False
game_won = False
first_guess = False

def same_letter():
    if guess_list.count(user_guess) > 1:
        guess_list.remove(user_guess)
    same_letter_list.append(user_guess)
    print(f"You already guessed this letter: '{user_guess}'. Guess another one.")

start = input("Type 'Start' to begin! ").lower()

while start == "start":
    word = random.choice(word_list)
    for blank in range(len(word)):
        blanks_list += ["_"]
        blanks_string = " ".join(blanks_list)
    print(blanks_string)
        
    while lives > 0 and not end_of_game and not game_won:
        user_guess = input("Guess a letter: ").lower()
        guess_list.append(user_guess)
        same_letter_list.append(user_guess)
        if guess_list.count(user_guess) >= 2:
            same_letter()
        if user_guess in word:
            for correct_letter in range(len(word)):
                if word[correct_letter] == user_guess:
                    blanks_list.pop(correct_letter)
                    new_letter = blanks_list.insert(correct_letter, user_guess)

        else:   
            if not first_guess and same_letter_list.count(user_guess) >= 2:
                if guess_list.count(user_guess) > 1:
                    guess_list.remove(user_guess)
                same_letter_list.append(user_guess)
            elif not first_guess:
                lives -= 1
                print(f"The letter '{user_guess}', is not in the word. You lost a life.")
                for life in range(lives):
                    if lives == life + 1:
                        print(hangman_logos.gallows[life])
                        if life == 0:
                            end_of_game = True

        print(f"Your guesses: {guess_list}")
        new_blanks = " ".join(blanks_list)
        print(new_blanks)

        if "_" not in new_blanks:
            end_of_game = True
            game_won = True
            print("You won. Game over.")
            os.system("pause")
            break

    if game_won:
        break
    if end_of_game and not game_won:
        print("You lose. Game over.")
        os.system("pause")
        break