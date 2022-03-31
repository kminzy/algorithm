import sys

N = int(sys.stdin.readline().rstrip())
rank = []
total = [i for i in range(1, N + 1)]
result = []

for i in range(N):
    rank.append(int(sys.stdin.readline().rstrip()))

rank = sorted(rank)

for i in range(N):
    result.append(abs(total[i] - rank[i]))

print(sum(result))