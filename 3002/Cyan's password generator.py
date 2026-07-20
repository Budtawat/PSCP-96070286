"""Cyan's password generator"""
name=input()
lname=input()
age=input()

if len(name) >= 5 and len(lname) >= 5:
    password = name[:2] + lname[-1] + age[-1]
else:
    password = name[0] + age + lname[-1]
print(password)
