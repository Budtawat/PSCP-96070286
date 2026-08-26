"""Arcade of Time : Store Check"""


def main():
    """Count number of open stores at specified query minutes using difference array"""
    num, _ = map(int, input().split())
    diff = [0] * 1442
    for _ in range(num):
        start, stop = map(int, input().split())
        diff[start] += 1
        diff[stop] -= 1
    open_stores = [0] * 1441
    current = 0
    for minute in range(1441):
        current += diff[minute]
        open_stores[minute] = current

    queries = list(map(int, input().split()))
    results = [str(open_stores[q]) for q in queries]

    print(" ".join(results))
main()
