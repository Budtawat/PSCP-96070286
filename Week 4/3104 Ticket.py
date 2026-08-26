"""Ticket"""
def ticket():
    """Ticket"""
    age, day = input().split()
    age = int(age)
    x = 0
    if day == "Wed":
        if age < 5:
            x = 0
        elif 5 <= age <= 18:
            x = 100 /2
        elif age >= 19:
            x = 150 /2
    else:
        if age < 5:
            x = 0
        elif 5 <= age <= 18:
            x = 100
        elif age >= 19:
            x = 150
    print(f"{x:.0f}")
ticket()
