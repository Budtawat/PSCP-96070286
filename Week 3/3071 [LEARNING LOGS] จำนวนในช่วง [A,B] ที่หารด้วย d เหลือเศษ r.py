"""Count Numbers with Remainder"""


def count_with_remainder(limit, divisor, remainder):
    """Count positive integers <= limit that have the given remainder"""
    if limit < remainder:
        return 0
    return (limit - remainder) // divisor + 1


def main():
    """Calculate the count of numbers in range [A, B] with remainder r when divided by d"""
    num_a = int(input())
    num_b = int(input())
    divisor_d = int(input())
    remainder_r = int(input())

    count_b = count_with_remainder(num_b, divisor_d, remainder_r)
    count_a = count_with_remainder(num_a - 1, divisor_d, remainder_r)

    print(count_b - count_a)
main()
