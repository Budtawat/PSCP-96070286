"""ภาษี"""

def tax():
    '''ภาษีรถยนต์'''
    year = int(input())
    cc = int(input())
    x = 0
    if year <= 1990:
        if cc <= 1500:
            x = 1250
        elif 1500 < cc <= 2000:
            x = 1400
        elif cc > 2000:
            x = 2000
    elif 1991 <= year <= 1999:
        if cc <= 1500:
            x = 1100
        elif 1500 < cc <= 2000:
            x = 1300
        elif cc > 2000:
            x = 1700
    elif year >= 2000:
        if cc <= 1500:
            x = 1000
        elif 1500 < cc <= 2000:
            x = 1200
        elif cc > 2000:
            x = 1500
    print(x)
tax()
