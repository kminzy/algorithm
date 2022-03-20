import sys
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx와 ny가 범위 내에 있고, 아직 토마토가 익지 않은 경우 방문
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())  # Y, X
    graph = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    queue = deque([])

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))

    bfs()

    Flag = False
    result = -1

    for g in graph:
        for tomato in g:
            if tomato == 0:
                Flag = True
            result = max(result, tomato)

    if Flag:  # 토마토가 모두 익지 못한 상태
        print(-1)
    elif result == 1:  # 저장될 때부터 모든 토마토가 익어있는 상태
        print(0)
    else:
        print(result - 1)