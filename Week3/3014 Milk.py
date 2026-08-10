"""Milk"""

price = int(input())
bot = int(input())
botton = int(input())
ownmoney = int(input())

total= (ownmoney // price)
a = total
while a >= bot:
    total += a // bot
