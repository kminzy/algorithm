import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
graph = []

count = 0
count_rgb = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))


def dfs(x, y):
    global count, count_rgb
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                dfs(nx, ny)


visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)

for i in range(n): # G의 노드를 R로 변환해서 그래프 갱신
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)] # 적록색약의 경우 다시 그래프 돌기 위해 visited 초기화

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            count_rgb += 1

print(count_rgb)
