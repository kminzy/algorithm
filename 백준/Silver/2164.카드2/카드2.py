from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

queue = deque(list(i for i in range(1, n + 1)))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])