import os

print("Welcome to the Love Calculator!\n")
gender1 = input("What is your gender? Male or Female? ").lower()
gender2 = input("What is their gender? Male or Female? ").lower()
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
zodiac1 = input("What is your zodiac sign? ").lower()
zodiac2 = input("What is their zodiac sign? ").lower()

zodiac_list = []

ariesf = 0
taurusf = 0
geminif = 0
cancerf = 0
leof = 0
virgof = 0
libraf = 0
scorpiof = 0
sagittariusf = 0
capricornf = 0
aquariusf = 0
piscesf = 0
ariesm = 0
taurusm = 0
geminim = 0
cancerm = 0
leom = 0
virgom = 0
libram = 0
scorpiom = 0
sagittariusm = 0
capricornm = 0
aquariusm = 0
piscesm = 0

if gender1 == "female":
    if zodiac1 == "aries":
        ariesf = 1.99
        zodiac_list += [ariesf]
    if zodiac1 == "taurus":
        taurusf = 1.67
        zodiac_list += [taurusf]
    if zodiac1 == "gemini":
        geminif = 2.143
        zodiac_list += [geminif]
    if zodiac1 == "cancer":
        cancerf = 1.98493
        zodiac_list += [cancerf]
    if zodiac1 == "leo":
        leof = 2.1463
        zodiac_list += [leof]
    if zodiac1 == "virgo":
        virgof = 1.8046
        zodiac_list += [virgof]
    if zodiac1 == "libra":
        libraf = 1.95
        zodiac_list += [libraf]
    if zodiac1 == "scorpio":
        scorpiof = 1.55
        zodiac_list += [scorpiof]
    if zodiac1 == "sagittarius":
        sagittariusf = 2.011
        zodiac_list += [sagittariusf]
    if zodiac1 == "capricorn":
        capricornf = 2.1
        zodiac_list += [capricornf]
    if zodiac1 == "aquarius":
        aquariusf = 1.9643
        zodiac_list += [aquariusf]
    if zodiac1 == "pisces":
        piscesf = 2.12
        zodiac_list += [piscesf]
elif gender1 == "male":
    if zodiac1 == "aries":
        ariesm = 1.801
        zodiac_list += [ariesm]
    if zodiac1 == "taurus":
        taurusm = 1.7964
        zodiac_list += [taurusm]
    if zodiac1 == "gemini":
        geminim = 2.0998
        zodiac_list += [geminim]
    if zodiac1 == "cancer":
        cancerm = 1.98999
        zodiac_list += [cancerm]
    if zodiac1 == "leo":
        leom = 2.1199
        zodiac_list += [leom]
    if zodiac1 == "virgo":
        virgom = 2.355
        zodiac_list += [virgom]
    if zodiac1 == "libra":
        libram = 2.1025
        zodiac_list += [libram]
    if zodiac1 == "scorpio":
        scorpiom = 1.613
        zodiac_list += [scorpiom]
    if zodiac1 == "sagittarius":
        sagittariusm = 1.9393
        zodiac_list += [sagittariusm]
    if zodiac1 == "capricorn":
        capricornm = 2.262
        zodiac_list += [capricornm]
    if zodiac1 == "aquarius":
        aquariusm = 1.96
        zodiac_list += [aquariusm]
    if zodiac1 == "pisces":
        piscesm = 2.17
        zodiac_list += [piscesm]

if gender2 == "female":
    if zodiac2 == "aries":
        ariesf = 1.99
        zodiac_list += [ariesf]
    if zodiac2 == "taurus":
        taurusf = 1.67
        zodiac_list += [taurusf]
    if zodiac2 == "gemini":
        geminif = 2.143
        zodiac_list += [geminif]
    if zodiac2 == "cancer":
        cancerf = 1.98493
        zodiac_list += [cancerf]
    if zodiac2 == "leo":
        leof = 2.1463
        zodiac_list += [leof]
    if zodiac2 == "virgo":
        virgof = 1.8046
        zodiac_list += [virgof]
    if zodiac2 == "libra":
        libraf = 1.95
        zodiac_list += [libraf]
    if zodiac2 == "scorpio":
        scorpiof = 1.55
        zodiac_list += [scorpiof]
    if zodiac2 == "sagittarius":
        sagittariusf = 2.011
        zodiac_list += [sagittariusf]
    if zodiac2 == "capricorn":
        capricornf = 2.1
        zodiac_list += [capricornf]
    if zodiac2 == "aquarius":
        aquariusf = 1.9643
        zodiac_list += [aquariusf]
    if zodiac2 == "pisces":
        piscesf = 2.12
        zodiac_list += [piscesf]
elif gender2 == "male":
    if zodiac2 == "aries":
        ariesm = 1.801
        zodiac_list += [ariesm]
    if zodiac2 == "taurus":
        taurusm = 1.7964
        zodiac_list += [taurusm]
    if zodiac2 == "gemini":
        geminim = 2.0998
        zodiac_list += [geminim]
    if zodiac2 == "cancer":
        cancerm = 1.98999
        zodiac_list += [cancerm]
    if zodiac2 == "leo":
        leom = 2.1199
        zodiac_list += [leom]
    if zodiac2 == "virgo":
        virgom = 2.355
        zodiac_list += [virgom]
    if zodiac2 == "libra":
        libram = 2.1025
        zodiac_list += [libram]
    if zodiac2 == "scorpio":
        scorpiom = 1.613
        zodiac_list += [scorpiom]
    if zodiac2 == "sagittarius":
        sagittariusm = 1.9393
        zodiac_list += [sagittariusm]
    if zodiac2 == "capricorn":
        capricornm = 2.262
        zodiac_list += [capricornm]
    if zodiac2 == "aquarius":
        aquariusm = 1.96
        zodiac_list += [aquariusm]
    if zodiac2 == "pisces":
        piscesm = 2.17
        zodiac_list += [piscesm]

names_combined = name1 + name2

true_count = 0
love_count = 0
love_score = 0

for char in range(len(names_combined)):
    if names_combined[char] == "t":
        true_count += 1
    if names_combined[char] == "r":
        true_count += 1
    if names_combined[char] == "u":
        true_count += 1
    if names_combined[char] == "e":
        true_count += 1
        love_count += 1
    if names_combined[char] == "l":
        love_count += 1
    if names_combined[char] == "o":
        love_count += 1
    if names_combined[char] == "v":
        love_count += 1

zodiac_success_percent = (zodiac_list[0] * zodiac_list[1] / 5)

love_score = round(zodiac_success_percent * (true_count * 10 + love_count) + (true_count * 10 + love_count))

if love_score < 10 or love_score > 90:
    print(f"Your love score is: {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your love score is: {love_score}, you are alright together.")
else:
    print(f"Your love score is: {love_score}.")
os.system("pause")