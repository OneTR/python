words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
last_letters = [letter[-1] for letter in words]
other_letters = [letter[:-1] for letter in words]

for char in range(len(last_letters)):
    if last_letters[char] == "e":
        past_tense = past_tense + [other_letters[char] + last_letters[char] + "d"]
    else:
        past_tense = past_tense + [other_letters[char] + last_letters[char] + "ed"]

print(past_tense)

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = 0

for char in s:
    if char in vowels:
        num_vowels += 1

print(num_vowels)

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
words = sentence.split()
same_letter_count = 0
first_letters = [letter[0] for letter in words]
last_letters = [letter[-1] for letter in words]

for char in range(len(words)):
    if first_letters[char] == last_letters[char]:
        same_letter_count += 1

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
words = sentence.split()

for char in range(len(words)):
    if "a" in words[char] or "e" in words[char]:
        num_a_or_e += 1