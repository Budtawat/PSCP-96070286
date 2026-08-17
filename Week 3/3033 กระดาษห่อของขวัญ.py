"""กระดาษห่อของขวัญ"""

PI = 3.14

r, h, glue = map(float, input().split())

width = h + 2 * r
length = 2 * PI * r + glue

print(f"{width:.2f} {length:.2f}")
