"""Pair Numbering."""

import json


def count_pairs(list_a, list_b, target_sum):
    """Count number of pairs from list_a and list_b summing to target_sum."""
    freq_b = {}
    for num in list_b:
        freq_b[num] = freq_b.get(num, 0) + 1

    total_pairs = 0
    for num in list_a:
        needed = target_sum - num
        total_pairs += freq_b.get(needed, 0)

    return total_pairs


def main():
    """Run program."""
    list_a = json.loads(input().strip())
    list_b = json.loads(input().strip())
    target_sum = int(input().strip())
    print(count_pairs(list_a, list_b, target_sum))


main()
