"""Express Delivery Shipping Fee Calculation"""


def main():
    """Calculate total shipping cost based on origin, destination, and weight"""
    line1 = input().split()
    origin = line1[0]
    destination = line1[1]
    weight = float(input())

    routes = {
        ("BKK", "CNX"): (10, 30),
        ("CNX", "UBP"): (15, 40),
        ("UBP", "BKK"): (20, 40),
        ("BKK", "PKT"): (25, 50),
        ("PKT", "CNX"): (30, 60),
        ("UBP", "PKT"): (40, 70),
    }

    key = (origin, destination)
    if key in routes:
        base_fee, weight_rate = routes[key]
        total_cost = base_fee + (weight_rate * weight)
        print(f"{total_cost:.2f}")
    else:
        print("Error")
main()
