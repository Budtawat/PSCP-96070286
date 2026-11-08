"""Stair"""

def main():
    """Calculate the minimum steps to reach the top."""
    y = int(input())
    n = int(input())

    steps = 0
    current_sum = 0
    possible = True

    for _ in range(n):
        height = int(input())
        if height > y:
            possible = False

        if current_sum + height <= y:
            current_sum += height
        else:
            steps += 1
            current_sum = height

    if current_sum > 0:
        steps += 1

    if not possible:
        print("NO")
    else:
        print(steps)


if __name__ == "__main__":
    main()
