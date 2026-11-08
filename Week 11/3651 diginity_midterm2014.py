"""Diginity Midterm2014."""


def get_digital_root(num_str):
    """Calculate single digit sum from string."""
    while len(num_str) > 1:
        total = 0
        for char in num_str:
            total += int(char)
        num_str = str(total)
    return num_str


def main():
    """Run program."""
    while True:
        card_id = input().strip()
        if card_id == "0":
            break
        print(get_digital_root(card_id))


main()
