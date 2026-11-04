"""Phone number formatting."""

def main():
    """Format phone number."""
    phone = input().strip()
    category = input().strip()

    mid_digits = phone[-8:-4]
    last_digits = phone[-4:]
    if category == "Domestic":
        prefix = phone[:-8]
    else:
        prefix = "+66" + phone[1:-8]
    print(prefix, mid_digits, last_digits)

main()
