n = 0
remainder = 0

while True:
    n = n + 1
    remainder = (remainder * 10 + 1) % 2003

    if remainder == 0:
        print(n)
        break