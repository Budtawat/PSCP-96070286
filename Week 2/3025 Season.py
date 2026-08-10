"""Season"""
month = int(input())
day = int(input())

winter=[1,2,3]
spring=[4,5,6]
summer=[7,8,9]
fall=[10,11,12]

if month in winter:
    PRE = "winter"
elif month in spring:
    PRE = "spring"
elif month in summer:
    PRE = "summer"
elif month in fall:
    PRE = "fall"
else:
    PRE = ""

if not month %3 and PRE == "winter" and day >= 21:
    print("spring")
elif not month %3 and PRE == "spring" and day >= 21:
    print("summer")
elif not month %3 and PRE == "summer" and day >= 21:
    print("fall")
elif not month %3 and PRE == "fall" and day >= 21:
    print("winter")
else:
    print(PRE)
