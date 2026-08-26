"""Promotion Price Calculation"""


def main():
    """Calculate total price with 10% discount if 3 or more items purchased"""
    pencil_a, notebook_b, color_box_c = map(int, input().split())

    total_items = pencil_a + notebook_b + color_box_c
    total_price = (pencil_a * 25) + (notebook_b * 40) + (color_box_c * 55)

    if total_items >= 3:
        total_price = int(total_price * 0.9)

    print(total_price)
main()
