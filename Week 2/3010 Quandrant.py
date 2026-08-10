"""Quadrant"""
x = int(input())
y = int(input())

if not x:
    if not y:
        print("O")
    else:
        print("Y")
elif not y:
    print("X")
elif x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
else:
    if y > 0:
        print("Q2")
    else:
        print("Q3")
