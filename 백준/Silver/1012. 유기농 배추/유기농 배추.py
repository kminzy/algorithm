import sys

sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global count
    visited[x][y] = 1  # 방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and graph[nx][ny] == 'V':
                dfs(nx, ny)


for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        u, v = map(int, sys.stdin.readline().split())
        graph[v][u] = 'V'

    for j in range(N):
        for k in range(M):
            if visited[j][k] == 0 and graph[j][k] == 'V':
                count += 1
                dfs(j, k)

    print(count)
