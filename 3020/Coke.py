"""Coke"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

caps = 0
total_cost = 0

for _ in range(d):
    if b > 0 and caps >= b:
        caps -= b
        total_cost += c
    else:
        total_cost += a
    caps += 1

print(total_cost)
