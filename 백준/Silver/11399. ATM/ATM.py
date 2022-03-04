import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))
moneyTime = dict()
minTime = []
current = 0

for i in range(N):  # key는 사람의 번호, value는 인출 시간
    moneyTime[i + 1] = P[i]

moneyTime = dict(sorted(moneyTime.items(), key=lambda x: x[1]))

for value in moneyTime.values():
    current += value
    minTime.append(current)

print(sum(minTime))