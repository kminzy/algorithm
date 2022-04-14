from collections import deque
import sys


def dfs(node):
    visited[node] = 1

    print(node, end=' ')

    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)
    return


def bfs(node):
    visited[node] = 1
    q.append(node)

    while q:
        target = q.popleft()
        print(target, end=' ')

        for i in graph[target]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    return


if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())
    graph = dict()
    q = deque()

    for i in range(n):
        graph[i + 1] = list()

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for value in graph.values():
        value.sort()

    visited = [0 for _ in range(n + 1)]
    dfs(v)
    print()
    visited = [0 for _ in range(n + 1)]
    bfs(v)