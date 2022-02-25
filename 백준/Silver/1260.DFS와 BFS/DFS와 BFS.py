from collections import deque
import sys

def dfs(node):
    d_visited[node] = 1

    print(node, end=' ')

    for i in graph[node]:
        if d_visited[i] == 0:
            dfs(i)
    return

def bfs(node):
    b_visited[node] = 1

    queue.append(node)

    while queue:
        target = queue.popleft()

        print(target, end=' ')

        for j in graph[target]:
            if b_visited[j] == 0:
                b_visited[j] = 1
                queue.append(j)
    return

if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())
    graph = dict()
    queue = deque()

    d_visited = [0 for _ in range(n + 1)]
    b_visited = [0 for _ in range(n + 1)]

    for i in range(n):
        graph[i+1] = list()

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for value in graph.values():
        value.sort()

    dfs(v)
    print()
    bfs(v)