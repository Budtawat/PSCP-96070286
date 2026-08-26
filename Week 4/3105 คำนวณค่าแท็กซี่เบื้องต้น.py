"""คำนวณค่าแท็กซี่เบื้องต้น"""
def main():
    """คำนวณค่าแท็กซี่เบื้องต้น"""
    dis = int(input())
    x=0
    for i in range(1, dis+1):
        if i <= 1:
            x += 35
        elif i <= 10:
            x += 5
        else:
            x += 8
    print(x)
main()
