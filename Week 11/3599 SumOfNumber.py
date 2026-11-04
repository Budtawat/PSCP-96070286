"""SumOfNumber"""

target = int(input())
total = 0
while True:
    num = int(input())
    if num == -1:
        break
    total += num
    if total == target:
        break
print(total)
