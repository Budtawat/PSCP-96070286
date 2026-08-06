"""Calculator"""

n = int(input())

if n == 1:
    print(1)
else:
    digit_count = sum(len(str(i)) for i in range(1, n + 1))
    
    total_presses = digit_count + n
    print(total_presses)
