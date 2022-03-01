from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

queue = deque(list(range(1, n + 1)))
result = []

while queue:
    queue.rotate(-k + 1)
    result.append(queue.popleft())

result = map(str, result)

print("<", end='')
print(', '.join(result), end='')
print(">", end='')