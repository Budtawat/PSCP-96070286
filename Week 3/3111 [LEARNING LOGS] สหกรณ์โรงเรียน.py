"""School Cooperative Discount Calculation"""
from decimal import Decimal, ROUND_HALF_UP


def main():
    """Calculate net total price after discount using round half up"""
    is_member = input().strip().upper()
    item_count = int(input().strip())

    total = Decimal("0")
    for _ in range(item_count):
        total += Decimal(input().strip())

    if is_member == "Y":
        discount_rate = Decimal("0.05")
    elif is_member == "N" and total >= Decimal("500"):
        discount_rate = Decimal("0.03")
    else:
        discount_rate = Decimal("0")

    net_total = total * (Decimal("1") - discount_rate)
    result = net_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print(f"{result:.2f}")
main()
