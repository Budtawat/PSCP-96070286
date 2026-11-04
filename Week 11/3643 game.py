"""Game"""

def main():
    """Find minimum draws"""
    score_a = int(input())
    score_b = int(input())
    if score_a >= 0 and score_b >= 0 and score_a % 3 == score_b % 3:
        print(score_a % 3)
    else:
        print("Error")

main()
