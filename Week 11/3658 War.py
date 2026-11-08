"""War"""

import re

def main():
    """Run program."""
    our_team = [int(x) for x in re.findall(r"\d+", input())]
    enemy_team = [int(x) for x in re.findall(r"\d+", input())]

    our_team.sort(reverse=True)
    enemy_team.sort(reverse=True)
    total_score = 0
    j = 0
    n = len(enemy_team)
    for point in our_team:
        while j < n and enemy_team[j] >= point:
            j += 1

        if j < n:
            total_score += point
            j += 1
    print(total_score)
if __name__ == "__main__":
    main()
