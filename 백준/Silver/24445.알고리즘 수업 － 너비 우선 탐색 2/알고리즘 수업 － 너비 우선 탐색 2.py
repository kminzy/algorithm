import sys
from collections import deque


def bfs(node):
    global order
    queue.append(node)
    visited[node] = order

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if visited[i] == 0:
                order += 1
                visited[i] = order
                queue.append(i)
    return


if __name__ == "__main__":
    n, m, r = map(int, sys.stdin.readline().split())
    graph = dict()
    visited = [0 for _ in range(n + 1)]
    queue = deque()
    order = 1

    for i in range(n):
        graph[i + 1] = list()

    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for value in graph.values():
        value.sort(reverse=True)

    bfs(r)

    for o in range(1, len(visited)):
        print(visited[o])