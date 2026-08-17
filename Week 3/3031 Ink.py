"""Ink"""

import math

PI = 3.1416

s, n = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    d_sq = x ** 2 + y ** 2
    t = PI * d_sq / s
    print(math.ceil(t - 1e-9))
