"""น้อยสูงสุด(4ค่า)"""

n = int(input())

for i in range(n):
    num = int(input())
    if not i:
        result = num
    elif num < result:
        result = num

print(result)
