"""Milk"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

milk = d // a

if b:
    caps = milk

    while caps >= b:
        exchange = caps // b
        milk += exchange * c
        caps = caps % b + exchange * c

print(milk)
