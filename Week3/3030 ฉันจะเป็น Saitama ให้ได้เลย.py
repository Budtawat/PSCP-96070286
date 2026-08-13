"""ฉันจะเป็น Saitama ให้ได้เลย"""

import math

pushup_t, situp_t, squat_t, run_t = [int(input()) for _ in range(4)]
pushup_r, situp_r, run_r, squat_r = [int(input()) for _ in range(4)]

days = max(
    math.ceil(pushup_t / pushup_r),
    math.ceil(situp_t / situp_r),
    math.ceil(squat_t / squat_r),
    math.ceil(run_t / run_r)
)

print(days)
