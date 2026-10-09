"""Star"""
n = int(input())

# คำนวณจำนวนดอกจันในแต่ละบรรทัด หากน้อยกว่า 1 ให้เป็น 0 (ไม่แสดงดอกจัน)
count1 = max(0, n)
count2 = max(0, n - 2)
count3 = max(0, n - 4)

# แสดงผลลัพธ์ทั้ง 3 บรรทัด
print("*" * count1)
print("*" * count2)
print("*" * count3)
