"""Coke"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

caps = 0
total_cost = 0
i = 0
while i < d:
    if 0 < b <= caps:
        caps -= b
        total_cost += c
    else:
        total_cost += a
    caps += 1
    i += 1

print(total_cost)
