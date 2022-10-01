from letters import alphabet, letters, symbols # Needed variables from letters.py
from cipher_art import logo # Needed logo cipher_art.py
from os import system

print(logo)

# The main function
def caesar(start_text, shift_amount, cipher_direction): # start_text is the main input that user gives. shift_amount is the amount of shift to cipher words. cipher_direction is the variable that determines whether the encoding or decoding is going to be done.
    symbol_list = symbols.split(" ") # The symbols that comes from letters.py
    text_letters = list(start_text) # The main list that contains letters from the main input.
    txt_w_symbol = start_text # The variable that used for checking if the input has symbols.
    words = [] # An empty list used to divide multiple words if there are multiple words in the input.
    end_text = "" # An empty string that will be ciphered.
    ciphered_msg = "" # If the main input has spaces this empty string will be the ciphered text.
    
    # To reduce the shift amount by mod 26 if the amount is too high.
    if shift_amount > 26:
        shift_amount %= 26
    elif shift_amount == 26:
        shift_amount = (shift_amount % 26) + 1

    # To determine the symbols' locations in the input and remove them from the input temporarily.
    for symbol in symbol_list:
        if symbol in text_letters:
            sym_lctn = text_letters.index(symbol)
            text_letters.pop(sym_lctn)

    # If the decode function is selected, this if statement will apply.
    if cipher_direction == "decode":
        shift_amount *= -1
    
    # If the input has spaces, this if statement will locate the space and remove from the input temporarily.
    if " " in text_letters:
        lctn_space = text_letters.index(" ")
        words += text_letters[0:lctn_space] + text_letters[lctn_space + 1:len(text_letters)]
        start_text = "".join(words)
    else:
        start_text = "".join(text_letters)
    
    # This is the ciphering process.
    for letter in start_text:
        position = alphabet.index(letter)  
        new_position = position + shift_amount

        # If the letters in the input is too close to the end of the alphabet, this if statement will make the cipher go to the start of the alphabet.
        if new_position >= 26:
            last_position = 26 - position
            new_position = shift_amount - last_position
            new_letter = alphabet[new_position]

        # Ciphering process
        new_letter = alphabet[new_position]
        end_text += new_letter
    
    # Assigning end_text to ciphered_txt in order to check spaces.
    ciphered_txt = list(end_text)
        
    # Inserting symbols to the text after ciphering.
    for symbol in symbol_list:
        if symbol in txt_w_symbol:
            ciphered_txt.insert(sym_lctn, symbol)
    
    # Inserting the space to the text to its location after ciphering.
    if " " in text_letters:
        ciphered_txt.insert(lctn_space, " ")
        ciphered_msg = "".join(ciphered_txt)
        print(f"Here's the {cipher_direction}d result: {ciphered_msg}")
    else:
        ciphered_msg = "".join(ciphered_txt)
        print(f"Here's the {cipher_direction}d result: {ciphered_msg}")

# This checks whether the user wants to continue ciphering.
should_continue = True

# This loop will continue forever until the user want to exit the program.
while should_continue:
    # The parameters that is used in the main function.
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt\n").lower()
    msg = input("Type your message:\n").lower()
    shift_amt = int(input("Type the shift number:\n"))

    # The main function with its arguments.
    caesar(start_text=msg, shift_amount=shift_amt, cipher_direction=direction)
    
    # The prompt that asks the user if they want to continue.
    prompt = input("Do you want to cipher another word(s)?\n").lower()
    
    # If they don't want to continue ciphering, this if statement will apply.
    if prompt == "no":
        should_continue = False
        print("Goodbye!")
        system("pause")