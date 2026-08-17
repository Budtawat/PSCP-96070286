"""คะแนนสอบ"""

n = int(input())
scores = [int(input()) for _ in range(n)]

top_score = max(scores)
top_count = scores.count(top_score)

print(top_score)
print(top_count)
