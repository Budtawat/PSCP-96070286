"""ปราสาท"""
import sys
from math import isqrt
from collections import deque


def get_row(x: int) -> int:
    """หาว่าห้องหมายเลข x อยู่แถวที่เท่าไร
    แถว r ครอบคลุมห้องหมายเลข (r-1)^2 + 1 ถึง r^2
    """
    r = isqrt(x - 1) + 1
    return r


def solve(N: int) -> int:
    if N <= 1:
        return 0

    dist = [-1] * (N + 1)
    dist[1] = 0
    q = deque([1])

    while q:
        x = q.popleft()
        r = get_row(x)
        j = x - (r - 1) * (r - 1)
        row_max = 2 * r - 1

        neighbors = []


        if j > 1:
            neighbors.append(x - 1)


        if j < row_max and x + 1 <= N:
            neighbors.append(x + 1)


        if j % 2 == 0:
            nb = (r - 2) * (r - 2) + (j - 1)
            if 1 <= nb <= N:
                neighbors.append(nb)


        if j % 2 == 1:
            nb = r * r + (j + 1)
            if nb <= N:
                neighbors.append(nb)

        for nb in neighbors:
            if dist[nb] == -1:
                dist[nb] = dist[x] + 1
                q.append(nb)

    return dist[N] if dist[N] != -1 else 0


def main():
    N = int(sys.stdin.readline())
    print(solve(N))


if __name__ == "__main__":
    main()
