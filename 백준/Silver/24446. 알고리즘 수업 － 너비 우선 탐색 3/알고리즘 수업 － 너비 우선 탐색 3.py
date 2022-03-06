import sys
from collections import deque


def bfs(node):
    visited[node] += 1
    queue.append(node)

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[target] + 1


if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split())
    graph = dict()
    queue = deque()
    visited = [-1 for _ in range(N + 1)]

    for i in range(N):
        graph[i + 1] = list()

    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    bfs(R)

    for v in visited[1:]:
        print(v)
