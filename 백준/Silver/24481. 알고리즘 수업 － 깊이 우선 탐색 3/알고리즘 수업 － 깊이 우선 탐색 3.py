import sys
sys.setrecursionlimit(10**6)

def dfs(parent):
    global depth
    visited[parent] = depth # 들어온 노드에 방문처리

    for child in graph[parent]: # 노드의 자식들
        if visited[child] == -1:
            depth = visited[parent] + 1
            dfs(child)
    return


if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split())
    graph = dict()
    visited = [-1 for _ in range(N + 1)]
    depth = 0

    for i in range(N):
        graph[i + 1] = list()

    for j in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for value in graph.values():
        value.sort()

    dfs(R)

    for v in visited[1:]:
        print(v)