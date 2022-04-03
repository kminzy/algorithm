import sys

n = int(sys.stdin.readline().rstrip())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))[:len(road)] # 맨 마지막의 가격은 고려 x
total = 0
minPrice = price[0]

for i in range(len(road)):
    if minPrice > price[i]:
        minPrice = price[i]
    total += road[i] * minPrice

print(total)