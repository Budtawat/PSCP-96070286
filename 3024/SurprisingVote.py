"""SurprisingVote"""

total_score = float(input())
max_score = float(input())

min_possible_score = total_score - (2 * max_score)

if min_possible_score < 0:
    min_possible_score = 0.0
if (max_score - min_possible_score) > 2.0:
    print("Surprising")
else:
    print("Not surprising")
