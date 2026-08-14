"""รหัสแฝดเทค"""

id = int(input())
std1 = int(input())
std2 = int(input())

list1 = []
list2 = []
count = 0
count2 = 0
std1 = str(std1)
std2 = str(std2)
for i in range(id):
    list1.append(std1[i])
    list2.append(std2[i])
for j in range(id):
    if int(list1[j]) + int(list2[j]) == 9:
        count += 1
    else:
        count2 += 1
if count == id:
    print("YES")
else:
    print(f"NO {count2}")