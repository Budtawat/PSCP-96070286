"""ฟิลเตอร์ AR TikTok"""

r, x, y = map(int, input().split())

dist_sq = x ** 2 + y ** 2
r_sq = r ** 2

if dist_sq < r_sq:
    print("IN")
elif dist_sq == r_sq:
    print("ON")
else:
    print("OUT")
