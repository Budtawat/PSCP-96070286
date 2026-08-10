"""สถานะน้ำ"""

temp = int(input())
unit = input().upper()
temp_unit = 0
if unit == "C":
    temp_unit = temp
elif unit == "F":
    temp_unit = (temp - 32) * 5 / 9

if temp_unit <= 0:
    print("solid")
elif 0 < temp_unit < 100:
    print("liquid")
else:
    print("gas")
