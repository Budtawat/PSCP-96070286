"""Make Bridge"""


def main():
    """Calculate minimum small bricks needed to reach the goal length"""
    small_bricks = int(input())
    big_bricks = int(input())
    goal = int(input())

    # ใช้อิฐก้อนใหญ่ (5 นิ้ว) ให้ได้มากที่สุดโดยไม่เกิน goal
    big_used = min(big_bricks, goal // 5)
    remaining = goal - (big_used * 5)

    # ตรวจสอบว่าอิฐก้อนเล็ก (1 นิ้ว) เพียงพอกับระยะที่เหลือหรือไม่
    if remaining <= small_bricks:
        print(remaining)
    else:
        print(-1)
main()
