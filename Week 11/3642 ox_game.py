"""OX Game."""


def main():
    """Determine OX winner."""
    row1 = input().strip()
    row2 = input().strip()
    row3 = input().strip()

    lines = [
        row1,
        row2,
        row3,
        row1[0] + row2[0] + row3[0],
        row1[1] + row2[1] + row3[1],
        row1[2] + row2[2] + row3[2],
        row1[0] + row2[1] + row3[2],
        row1[2] + row2[1] + row3[0],
    ]

    if "OOO" in lines:
        print("O WIN")
    elif "XXX" in lines:
        print("X WIN")
    else:
        print("DRAW")


main()
