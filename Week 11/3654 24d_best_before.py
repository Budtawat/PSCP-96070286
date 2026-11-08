"""24D Best Before."""


def determine_date_format(count):
    """Determine whether date format is ddmmyy, mmddyy, or no clue."""
    found_ddmmyy = False
    found_mmddyy = False

    for _ in range(count):
        date_str = input().strip()
        first_num = int(date_str[:2])
        second_num = int(date_str[2:4])

        if 1 <= second_num <= 12 < first_num <= 31:
            found_ddmmyy = True
        elif 1 <= first_num <= 12 < second_num <= 31:
            found_mmddyy = True

    if found_ddmmyy and not found_mmddyy:
        return "ddmmyy"
    if found_mmddyy and not found_ddmmyy:
        return "mmddyy"
    return "no clue"


def main():
    """Run program."""
    total_bottles = int(input().strip())
    print(determine_date_format(total_bottles))


main()
