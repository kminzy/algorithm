import sys

n = int(sys.stdin.readline().rstrip())
graph = []
visited = [[0] * n for _ in range(n)] # n x n 배열 생성

# 상하좌우 좌표값
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
    global count
    visited[x][y] = 1 # 방문처리

    if graph[x][y] == 1: # 단지 내 집의 수 카운팅
        count += 1

    for i in range(4): # 상하좌우 체크
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n: # 좌표 조건 체크
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)

count = 0
count_list = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            dfs(i, j)
            count_list.append(count)
            count = 0 # 단지 완성되면 초기화

count_list.sort()
print(len(count_list))
for c in count_list:
    print(c)