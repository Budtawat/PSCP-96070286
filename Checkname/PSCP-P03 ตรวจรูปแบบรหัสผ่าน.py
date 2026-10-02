"""PSCP-P03 ตรวจรูปแบบรหัสผ่าน"""

password = input()

is_valid = True

if len(password) < 8:
    is_valid = False
else:
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
        elif "a" <= char <= "z":
            has_lower = True
        elif "0" <= char <= "9":
            has_digit = True
    if not (has_upper and has_lower and has_digit):
        is_valid = False
if is_valid:
    print("VALID")
else:
    print("INVALID")
