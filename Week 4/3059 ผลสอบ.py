"""Exam Result"""


def main():
    """Check if student passes all exam components"""
    exercise = float(input())
    midterm = float(input())
    final = float(input())

    if exercise >= 5 and midterm >= 20 and final >= 25:
        print("pass")
    else:
        print("fail")
main()
