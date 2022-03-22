import sys
from collections import deque


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        global cnt
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


if __name__ == "__main__":
    while True:
        w, h = map(int, sys.stdin.readline().split())  # x, y
        graph = []
        visited = [[0] * w for _ in range(h)]
        dx = [-1, 1, 0, 0, 1, -1, -1, 1]
        dy = [0, 0, -1, 1, 1, -1, 1, -1]
        cnt = 0

        if w == 0 and h == 0:
            break

        for i in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    bfs(i, j)
                    cnt += 1

        print(cnt)