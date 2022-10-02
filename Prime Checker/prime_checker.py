def prime_checker(number):
    remain_list = []
    for prime in range(1, number + 1):
        remain_list.append(number % prime)
        if remain_list.count(0) >= 3:
            is_prime = "It's not a prime number."
            break
        else:
            is_prime = "It's a prime number."
    print(is_prime)
    
n = int(input("Check this number: "))
prime_checker(number=n)