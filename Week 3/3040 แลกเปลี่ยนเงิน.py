"""แลกเปลี่ยนเงิน"""

amount = int(input())

coin10 = amount // 10
remain = amount % 10

coin5 = remain // 5
remain = remain % 5

coin2 = remain // 2
remain = remain % 2

coin1 = remain

print(f"10 = {coin10}")
print(f"5 = {coin5}")
print(f"2 = {coin2}")
print(f"1 = {coin1}")
