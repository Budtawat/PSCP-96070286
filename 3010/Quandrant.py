"""Quadrant"""
x = int(input())
y = int(input())

if not x and not y:
    print("O")
elif not y:
    print("X")
elif not x:
    print("Y")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
