"""Bubble Tea Calories Calculation"""


def main():
    """Calculate total calories of customized bubble tea"""
    line1 = input().split()
    pearl_type = line1[0].upper()
    pearl_amount = float(line1[1])

    line2 = input().split()
    tea_type = line2[0].upper()
    sweetness = int(line2[1])
    tea_volume = float(line2[2])

    pearl_rates = {"H": 5, "O": 3, "J": 2}
    pearl_cal = pearl_rates.get(pearl_type, 0) * pearl_amount

    tea_rates = {
        "R": {1: 12, 2: 18, 3: 25},
        "T": {1: 15, 2: 20, 3: 30},
        "M": {1: 10, 2: 15, 3: 20},
    }
    tea_cal = tea_rates.get(tea_type, {}).get(sweetness, 0) * tea_volume

    total = pearl_cal + tea_cal
    if total.is_integer():
        print(int(total))
    else:
        print(total)
main()
