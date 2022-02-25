from collections import deque
import sys

def bfs(node):
    visited[node] = 1

    queue.append(node)

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    return visited

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    graph = dict()
    queue = deque()
    visited = [0 for i in range(n + 1)]

    for i in range(n):
        graph[i + 1] = list()

    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    bfs(1)
    print(visited.count(1) - 1)