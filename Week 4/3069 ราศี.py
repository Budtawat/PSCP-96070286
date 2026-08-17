"""ราศี"""

date = int(input())
month = int(input())

if (month == 12 and date >=22 ) or (month == 1 and date <= 19):
    print("capricorn")
elif (month == 1 and date >=20 ) or (month == 2 and date <= 18):
    print("aquarius")
elif (month == 2 and date >=19 ) or (month == 3 and date <= 20):
    print("pisces")
elif (month == 3 and date >=21 ) or (month == 4 and date <= 19):
    print("aries")
elif (month == 4 and date >=20 ) or (month == 5 and date <= 20):
    print("taurus")
elif (month == 5 and date >=21 ) or (month == 6 and date <= 21):
    print("gemini")
elif (month == 6 and date >=22 ) or (month == 7 and date <= 22):
    print("cancer")
elif (month == 7 and date >=23 ) or (month == 8 and date <= 22):
    print("leo")
elif (month == 8 and date >=23 ) or (month == 9 and date <= 22):
    print("virgo")
elif (month == 9 and date >=23 ) or (month == 10 and date <= 23):
    print("libra")
elif (month == 10 and date >=24 ) or (month == 11 and date <= 21):
    print("scorpio")
elif (month == 11 and date >=22 ) or (month == 12 and date <= 21):
    print("sagittarius")
