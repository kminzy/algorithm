import sys

N, M = map(int, sys.stdin.readline().split())  # 사야 할 줄의 갯수, 브랜드 수
money = []
total = 0
min6 = 99999
min1 = 99999
min16 = 0

for i in range(M):
    money.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(money)):  # 묶음으로 살 때와 낱개로 살 때의 각각 최솟값
    min6 = min(min6, money[i][0])
    min1 = min(min1, money[i][1])

min16 = min1 * 6

while N:
    if N > 6:
        total += min(min6, min16)  # 묶음의 가격이 낱개 * 6보다 비싼 경우 고려
        N -= 6
    else:  # 6 이하
        if N * min1 > min6:
            total += min6
            N -= N
        else:
            total += N * min1
            N -= N

print(total)