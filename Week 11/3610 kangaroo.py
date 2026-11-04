"""Calculate maximum kangaroo jumps"""
def main():
    """Calculate maximum kangaroo jumps."""
    pos_a = int(input())
    pos_b = int(input())
    pos_c = int(input())

    gap_one = pos_b - pos_a - 1
    gap_two = pos_c - pos_b - 1
    if gap_one > gap_two:
        print(gap_one)
    else:
        print(gap_two)
main()
