"""กระต่ายน้อยล้อมรั้วลวดหนาม"""

width, length, layer = map(int, input().split())
price = int(input())

wire = 2 * (width + length) * layer
cost = wire * price

print(wire)
print(cost)
