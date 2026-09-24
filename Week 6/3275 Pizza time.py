"""Pizza time"""

import math


def main():
    """PAZZA TIME"""
    n = int(input())
    k = int(input())
    m = int(input())

    total_needed = n * k
    pizzas_to_order = math.ceil(total_needed / m)
    leftover = (pizzas_to_order * m) - total_needed

    print(total_needed)
    print(pizzas_to_order)
    print(leftover)


if __name__ == "__main__":
    main()
