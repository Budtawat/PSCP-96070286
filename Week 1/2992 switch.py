"""Switch"""
n = int(input())
op = input()

tens = n // 10
ones = n % 10
reverse = ones * 10 + tens

if op == "+":
    print(f"{n} + {reverse} = {n + reverse}")
else:
    print(f"{n} * {reverse} = {n * reverse}")
