"""BookWorm."""


def solve_case():
    """Solve a single test case for BookWorm."""
    total_time = float(input())
    book_count = int(input())

    books = [float(input()) for _ in range(book_count)]
    books.sort()

    read_count = 0
    time_spent = 0.0

    for duration in books:
        if time_spent + duration <= total_time:
            time_spent += duration
            read_count += 1
        else:
            break

    print(read_count)


def main():
    """Run all test cases."""
    num_cases = int(input())
    for _ in range(num_cases):
        solve_case()


main()
