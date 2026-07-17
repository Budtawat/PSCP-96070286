"""Hansib"""
num = int(input())

for i in range(num,-1,-1):
    if not i % 10:
        print(i, end=" ")