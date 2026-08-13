"""Rectangle Area"""

x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

overlap_width = min(x1 + w1, x2 + w2) - max(x1, x2)
overlap_height = min(y1 + h1, y2 + h2) - max(y1, y2)

if overlap_width > 0 and overlap_height > 0:
    print(overlap_width * overlap_height)
else:
    print("no overlapping")
