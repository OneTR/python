from letters import alphabet, letters

caesar_alphabet = letters.split(" ")

def caesar(message, shift, cipher_direction):
    text_letters = list(message)
    words = []
    encrypted_txt = ""

    if direction == "encode":
        if " " in text_letters:
            lctn_space = text_letters.index(" ")
            words += text_letters[0:lctn_space] + text_letters[lctn_space + 1:len(text_letters)]
            text_msg = "".join(words)
        else:
            text_msg = "".join(text_letters)

        encrypted_msg = ""

        for letter in text_msg:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position >= 26:
                last_position = 26 - position
                new_position = shift - last_position
                new_letter = alphabet[new_position]
            new_letter = alphabet[new_position]
            encrypted_txt += new_letter

        if " " in text_letters:
            encrypted_lst = list(encrypted_txt)
            encrypted_lst.insert(lctn_space, " ")
            encrypted_msg = "".join(encrypted_lst)
            print(encrypted_msg)
        else:
            print(encrypted_txt)

    elif direction == "decode":
        text_letters = list(message)
        words = []
        decrypted_txt = ""

        if " " in text_letters:
            lctn_space = text_letters.index(" ")
            words += text_letters[0:lctn_space] + text_letters[lctn_space + 1:len(text_letters)]
            text_msg = "".join(words)
        else:
            text_msg = "".join(text_letters)

        decrypted_msg = ""

        for letter in text_msg:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            decrypted_txt += new_letter

        if " " in text_letters:
            decrypted_lst = list(decrypted_txt)
            decrypted_lst.insert(lctn_space, " ")
            decrypted_msg = "".join(decrypted_lst)
            print(decrypted_msg)
        else:
            print(decrypted_txt)

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt\n").lower()
msg = input("Type your message:\n").lower()
shift_amt = int(input("Type the shift number:\n"))


caesar(message=msg, shift=shift_amt, cipher_direction=direction)