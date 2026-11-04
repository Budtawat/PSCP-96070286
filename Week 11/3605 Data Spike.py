"""Data Spike"""

def main():
    """Find maximum of 8 numbers."""
    max_num = 0
    for _ in range(8):
        num = int(input())
        if num > max_num:
            max_num = num
    print(max_num)
main()
