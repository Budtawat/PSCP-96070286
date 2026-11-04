"""BTSMRT."""

def main():
    """Check BTS/MRT fare status."""
    day_type = input().strip()
    age = float(input())
    height = float(input())

    is_small_child = age < 14 and height < 90
    is_children_day_free = day_type == "Children Day" and age < 14 and height <= 140
    is_senior_day_free = day_type == "Senior Day" and age >= 60

    if is_small_child or is_children_day_free or is_senior_day_free:
        print("FREE")
    else:
        print("PAY")
main()
