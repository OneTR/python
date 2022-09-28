num_list = []

for num in range(1, 101):
    num_list.append(num)
    if num_list[num - 1] % 3 == 0 and num_list[num - 1] % 5 != 0:
        num_list.remove(num)
        num_list.append("Fizz")
    elif num_list[num - 1] % 3 != 0 and num_list[num - 1] % 5 == 0:
        num_list.remove(num)
        num_list.append("Buzz")
    elif num_list[num - 1] % 3 == 0 and num_list[num - 1] % 5 == 0:
        num_list.remove(num)
        num_list.append("FizzBuzz")
    print(num_list[num - 1])

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)