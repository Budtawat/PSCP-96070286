"""Vowel Check"""


def main():
    """Check if the given character is a vowel"""
    char = input()

    if char in "aeiou":
        print("yes")
    else:
        print("no")
main()
