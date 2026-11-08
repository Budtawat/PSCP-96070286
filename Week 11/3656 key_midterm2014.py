"""Key Midterm2014."""


def calculate_key(citizen_id):
    """Calculate 4-digit key from 13-digit citizen ID."""
    digit_sum = 0
    for digit in citizen_id:
        digit_sum += int(digit)

    last_three_val = int(citizen_id[-3:]) * 10
    key = digit_sum + last_three_val

    if key > 9999:
        key %= 10000
    elif key < 1000:
        key += 1000

    return f"{key:04d}"


def main():
    """Run program."""
    citizen_id = input().strip()
    print(calculate_key(citizen_id))


main()
