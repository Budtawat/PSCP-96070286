"""Line Sorting."""


def sort_lines_by_length(count):
    """Read lines and sort them by length."""
    lines = []
    for _ in range(count):
        lines.append(input())
    lines.sort(key=len)
    for line in lines:
        print(line)


def main():
    """Run program."""
    total_lines = int(input())
    sort_lines_by_length(total_lines)


main()
