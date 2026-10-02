"""PSCP-P07 ยุบตัวอักษรที่ซ้ำติดกัน"""

text = input()
if text:
    result = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            result += text[i]
    print(result)
