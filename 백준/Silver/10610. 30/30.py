import sys

n = sys.stdin.readline().rstrip()
n = ''.join(sorted(n, reverse=True))

if int(n) % 30 == 0:
    print(int(n))
else:
    print(-1)