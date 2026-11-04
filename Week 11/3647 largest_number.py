"""Largest Number."""


def main():
    """Find greatest integer."""
    num_a = input().strip()
    num_b = input().strip()
    num_c = input().strip()

    opt1 = num_a + num_b + num_c
    opt2 = num_a + num_c + num_b
    opt3 = num_b + num_a + num_c
    opt4 = num_b + num_c + num_a
    opt5 = num_c + num_a + num_b
    opt6 = num_c + num_b + num_a

    best = opt1
    if opt2 > best:
        best = opt2
    if opt3 > best:
        best = opt3
    if opt4 > best:
        best = opt4
    if opt5 > best:
        best = opt5
    if opt6 > best:
        best = opt6

    if best[0] == "0":
        print(0)
    else:
        print(best)
main()
