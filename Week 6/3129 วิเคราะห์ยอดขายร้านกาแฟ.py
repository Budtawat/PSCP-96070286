"""วิเคราะห์ยอดขายร้านกาแฟ"""

def main():
    n = int(input())
    sales = [int(input()) for _ in range(n)]

    total_sales = sum(sales)
    max_sales = max(sales)
    min_sales = min(sales)
    avg_sales = total_sales / n

    print(total_sales)
    print(max_sales)
    print(min_sales)
    print(f"{avg_sales:.1f}")


if __name__ == "__main__":
    main()
