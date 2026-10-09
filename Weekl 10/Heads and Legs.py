"""Heads and Legs"""

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    if b % 2 != 0:
        print("Impossible")
        return 
    r = (b - 2 * a) // 2
    bird = a - r
    if r >= 0 and bird >= 0:
        print(f"{r} {bird}")
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
