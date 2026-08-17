"""ค่าน้อยสุด"""

a = int(input())
b = int(input())
c = int(input())

result = a
if b < result:
    result = b
if c < result:
    result = c

print(result)
