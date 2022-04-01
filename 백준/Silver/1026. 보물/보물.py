import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = 0

while b:
    result += max(b) * min(a)
    b.remove(max(b))
    a.remove(min(a))

print(result)