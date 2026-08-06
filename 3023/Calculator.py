"""Calculator"""

n = int(input())

if n == 1:
    print(1)
else:
    digits = 0
    for i in range(1, n + 1):
        digits += len(str(i))
    print(digits + n)
