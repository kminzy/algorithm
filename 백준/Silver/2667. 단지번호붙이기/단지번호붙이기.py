import sys

n = int(sys.stdin.readline().rstrip())
graph = []
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
count_list = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y):
    global count
    visited[x][y] = 1

    if graph[x][y] == 1:
        count += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            dfs(i, j)
            count_list.append(count)
            count = 0

count_list.sort()
print(len(count_list))
for c in count_list:
    print(c)
