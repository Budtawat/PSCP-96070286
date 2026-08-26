"""Bonus Calculation"""


def main():
    """Calculate total bonus based on position, experience, and salary"""
    data = input().split()
    pos = data[0]
    years = int(data[1])
    salary = int(data[2])

    if pos == "M":
        fixed_bonus = 1500
        if years > 10:
            rate_percent = 10
        elif years > 5:
            rate_percent = 8
        else:
            rate_percent = 6
    elif pos == "B":
        fixed_bonus = 1000
        if years > 10:
            rate_percent = 7
        elif years > 5:
            rate_percent = 6
        else:
            rate_percent = 5
    else:
        fixed_bonus = 500
        if years > 10:
            rate_percent = 6
        elif years > 5:
            rate_percent = 5
        else:
            rate_percent = 4

    total_bonus = fixed_bonus + (salary * rate_percent // 100)
    print(total_bonus)
main()
