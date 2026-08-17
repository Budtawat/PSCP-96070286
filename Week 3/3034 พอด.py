"""พอด"""

import sys

def solve():
    """อ่านข้อมูลและคำนวณจำนวนคนที่ยังรอในแถว"""
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1

    cnt = [0] * (K + 1)
    empty_queues = K

    for _ in range(N):
        c = int(data[idx])
        idx += 1
        cnt[c] += 1
        if cnt[c] == 1:
            empty_queues -= 1

        while not empty_queues:
            for j in range(1, K + 1):
                cnt[j] -= 1
                if not cnt[j]:
                    empty_queues += 1

    print(sum(cnt))


solve()
