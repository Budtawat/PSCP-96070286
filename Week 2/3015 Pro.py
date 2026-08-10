"""Pro"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())

group = z // x
remain = z % x

pay_people = group * y + remain
total = pay_people * a

print(total)
