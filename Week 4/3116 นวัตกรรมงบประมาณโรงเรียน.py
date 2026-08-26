"""Trash Bank School Password Key Generator"""


def main():
    """Generate a 6-digit password key based on school name"""
    school_name = input()

    first_char_ascii = ord(school_name[0].upper())
    last_char_ascii = ord(school_name[-1].upper())
    length = len(school_name)

    code = []
    for col in range(1, 11):
        place_val = col - 1

        if col % 2:
            val = first_char_ascii + place_val
        else:
            val = last_char_ascii - place_val

        rem = val % length
        if rem > 9:
            rem %= 10

        code.append(rem)

    result = code[2:8]
    print(*result)
main()
