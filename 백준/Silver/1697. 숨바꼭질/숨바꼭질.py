import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100000
visited = [0 for _ in range(MAX + 1)]


def bfs():
    queue = deque()
    queue.append(N)  # 시작지점 삽입

    while queue:
        target = queue.popleft()  # 타겟을 중심으로 bfs 수행

        if target == K:  # 동생 찾음
            print(visited[K])
            break

        child = [target + 1, target - 1, target * 2]  # 이동하는 세 가지 경우

        for c in child:
            if (0 <= c <= MAX) and visited[c] == 0:
                visited[c] = visited[target] + 1
                queue.append(c)


bfs()
