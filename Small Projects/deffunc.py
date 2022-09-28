import random

def square(x):
    return x * x

def sub(x, y):
    return x - y

def intdiv(x, y):
    return x // y

def div(x, y):
    return x / y

def add(x, y):
    return x + y

def mod(x, y):
    return x % y

def multi(x, y):
    return x * y

print(square(98))
print(sub(97, 58))
print(multi(add(889 - 54, intdiv(9753, 3)), mod(5784, square(25))))
print(div(48.85584, 3.952542))

print(intdiv)
print(type("Python!"))
print(type(3))
print(type(3.98))
print('''She said "I'm ready to learn Python!"''')
print("""I'm more
than ready.""")
print(int("79"))

for _ in range(3):
    print("3 times.")
    print("Anything?")

print("Not in the loop.")

randomFloat = random.random()
randomFloat *= 100
print(randomFloat)

diceThrow = random.randrange(1,7)
print(diceThrow)