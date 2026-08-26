"""Roman Numeral"""


def main():
    """Convert number 1-9 to Roman numeral with error handling"""
    num = int(input())

    if num < 0:
        print("Error : Please input positive number")
    elif not num or num > 9:
        print("Error : Out of range")
    else:
        roman_numerals = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        print(roman_numerals[num])
main()
