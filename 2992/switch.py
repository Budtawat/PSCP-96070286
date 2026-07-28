"""Switch"""
n = int(input())
op = input()

tens = n // 10
ones = n % 10

if op == "+":
    print(f"{tens} + {ones} = {tens + ones}")
elif op == "*":
    print(f"{tens} * {ones} = {tens * ones}")
