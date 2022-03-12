import sys

N, K = map(int, sys.stdin.readline().split())
money = []
count = []

for i in range(N):
    m = int(sys.stdin.readline().rstrip())
    money.append(m)

money = sorted(money, reverse=True)

for i in range(len(money)):
    c = K // money[i]
    count.append(c)
    K = K % money[i]

print(sum(count))