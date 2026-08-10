"""OverlapCircle"""

import math

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distance <= r1 + r2:
    print("overlapping")
else:
    print("no overlapping")
