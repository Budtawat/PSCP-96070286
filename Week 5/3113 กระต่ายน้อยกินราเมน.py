"""Ramen Price Calculation"""


def main():
    """Calculate total ramen price including toppings"""
    size, soup_type = input().split()
    size = size.upper()
    soup_type = soup_type.upper()

    topping_data = input().split()
    topping_type = topping_data[0].upper()

    ramen_prices = {
        "S": {"R": 60, "T": 80},
        "M": {"R": 80, "T": 100},
        "L": {"R": 100, "T": 120},
    }

    base_price = ramen_prices[size][soup_type]

    topping_price = 0
    if topping_type != "N":
        topping_count = int(topping_data[1])
        if topping_type == "P":
            topping_price = topping_count * 15
        elif topping_type == "E":
            topping_price = topping_count * 10

    total_price = base_price + topping_price
    print(total_price)
main()
