"""Basic ATM"""
def atm():
    """Basic ATM"""
    money = int(input())
    x = money // 1000
    money = money % 1000
    y = money // 500
    money = money % 500
    z = money // 100
    money = money % 100
    if not money:
        if x > 0:
            print(f"1000 : {x}")
        if y > 0:
            print(f"500 : {y}")
        if z > 0:
            print(f"100 : {z}")
    else:
        print("ERROR")
atm()
