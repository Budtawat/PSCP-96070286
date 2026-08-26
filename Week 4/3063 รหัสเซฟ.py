"""Safe Password"""


def main():
    """Verify safe character and digit password"""
    char = input()
    digit = int(input())

    char_correct = char == "H"
    digit_correct = digit == 4567

    if char_correct and digit_correct:
        print("safe unlocked")
    elif char_correct:
        print("safe locked - change digit")
    elif digit_correct:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
