import random

# 18 yazı 2 tura hesaplama %50 ihtimal üzerinden

coin = ["heads", "tails"]
flips = []
failed_try = 0
successful_try = 0
probability = []
tries = 10000

while failed_try < tries:
    for flip in range(20):
        flips = flips + [random.choice(coin)]
        if flips.count("heads") >= 3 or flips.count("heads") <= 1:
            failed_try += 1
            break
        elif flips.count("heads") == 2:
            successful_try += 1
            probability = probability + [1 / failed_try]
            break

result = sum(probability) / tries

print("%.9f" % result)