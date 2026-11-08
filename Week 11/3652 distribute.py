"""Distribute."""


def find_max_eights(money, children):
    """Find maximum number of children who can receive 8 baht."""
    if money < children:
        return -1

    if money == 8 * children:
        return children

    if money > 8 * children:
        return children - 1

    count_eight = (money - children) // 7
    rem_money = money - 8 * count_eight
    rem_children = children - count_eight

    if rem_children == 1 and rem_money == 4:
        count_eight -= 1

    return count_eight


def main():
    """Run program."""
    money = int(input())
    children = int(input())
    print(find_max_eights(money, children))


main()
