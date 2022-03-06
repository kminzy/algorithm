import sys
from collections import deque


def bfs(node):
    visited[node] += 1
    queue.append(node)

    while queue:
        parent = queue.popleft()

        for child in graph[parent]:
            if visited[child] == -1:
                queue.append(child)
                visited[child] = visited[parent] + 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())  # 노드
    a, b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())  # 간선
    graph = dict()
    visited = [-1 for _ in range(n + 1)]
    queue = deque()

    for i in range(n):
        graph[i + 1] = list()

    for i in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    bfs(a)

    if visited[a] == -1 or visited[b] == -1:
        print(-1)
    else:
        if a == b:
            print(1)
        else:
            print(visited[a] + visited[b])