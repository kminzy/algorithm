import sys

t = int(sys.stdin.readline().rstrip())
n = []

for i in range(t):
    n.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (max(n) + 1)  # dp list 초기화
dp[0], dp[1], dp[2] = 1, 2, 4

for j in range(3, max(n)):
    dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

for k in n:
    print(dp[k - 1])