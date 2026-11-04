"""RuleofThree"""

def main():
    """Find the best value snack."""
    total_items = int(input())
    best_price = float("inf")
    best_weight = 0.0
    max_value = -1.0

    for _ in range(total_items):
        price = float(input())
        weight = float(input())
        value = weight / price
        is_better = value - max_value > 1e-7
        is_tie_cheaper = abs(value - max_value) <= 1e-7 and price < best_price
        if is_better or is_tie_cheaper:
            max_value = value
            best_price = price
            best_weight = weight

    print(f"{best_price:.2f} {best_weight:.2f}")
main()
