"""รหัสแฝดเทค"""

id1 = int(input())
std1 = input()
std2 = input()

count = 0

for j in range(id1):
    if int(std1[j]) + int(std2[j]) != 9:
        count += 1
if not count:
    print("YES")
else:
    print(f"NO {count}")
