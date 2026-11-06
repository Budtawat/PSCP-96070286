"""B RNG."""


def get_gcd(val_a, val_b):
    """Calculate greatest common divisor."""
    while val_b:
        val_a, val_b = val_b, val_a % val_b
    return val_a


def get_cycle_sums(data, step_s, length, gcd_val, period):
    """Calculate sum for each cycle."""
    cycle_sums = [0] * gcd_val
    for cycle_idx in range(gcd_val):
        cycle_sums[cycle_idx] = sum(
            data[(cycle_idx + step_idx * step_s) % length]
            for step_idx in range(period)
        )
    return cycle_sums


def solve(data, total_n, step_s):
    """Calculate maximum sum."""
    length = len(data)
    gcd_val = get_gcd(step_s, length)
    period = length // gcd_val
    cycle_sums = get_cycle_sums(data, step_s, length, gcd_val, period)

    quotient, remainder = divmod(total_n, period)
    max_sum = None

    for start_idx in range(length):
        curr = start_idx
        rem_sum = 0
        for _ in range(remainder):
            rem_sum += data[curr]
            curr = (curr + step_s) % length
        curr_sum = quotient * cycle_sums[start_idx % gcd_val] + rem_sum

        if max_sum is None or curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


def main():
    """Run program."""
    raw_text = input().strip().strip("[]")
    data = [int(x) for x in raw_text.split(",") if x.strip()]
    print(solve(data, int(input()), int(input())))


main()
