"""Temperature"""
temp = float(input())
from_unit = input()
to_unit = input()

if from_unit == "C":
    c = temp
elif from_unit == "F":
    c = (temp - 32) * 5 / 9
elif from_unit == "K":
    c = temp - 273.15
elif from_unit == "R":
    c = temp * 5 / 9 - 273.15

if to_unit == "C":
    ans = c
elif to_unit == "F":
    ans = c * 9 / 5 + 32
elif to_unit == "K":
    ans = c + 273.15
elif to_unit == "R":
    ans = (c + 273.15) * 9 / 5

print(f"{ans:.2f}")