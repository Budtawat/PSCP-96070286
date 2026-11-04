"""how"""

male = 0
female = 0
while True:
    card = int(input())
    if card < 0:
        break
    if card % 2 == 1:
        male += 1
    else:
        female += 1
print(male, female, male + female)
