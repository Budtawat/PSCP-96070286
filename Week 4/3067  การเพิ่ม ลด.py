"""Check Sequence Order"""


def main():
    """Determine if three numbers are increasing, decreasing, or neither"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if num1 < num2 < num3:
        print("increasing")
    elif num1 > num2 > num3:
        print("decreasing")
    else:
        print("neither")
main()
