"""3nPlus1"""

while True:
    n = int(input())
    if not n:
        break
    count = 1
    while n != 1:
        if not n % 2:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    print(count)
