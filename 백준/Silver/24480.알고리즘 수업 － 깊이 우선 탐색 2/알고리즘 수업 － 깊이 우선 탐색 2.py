import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    global order
    visited[node] = order

    for i in graph[node]:
        if visited[i] == 0:
            order += 1
            dfs(i)

if __name__ == "__main__":
    n, m, r = map(int, sys.stdin.readline().split())
    graph = dict()
    visited = [0 for _ in range(n + 1)]
    order = 1

    for i in range(n):  # 노드의 수만큼 graph 생성
        graph[i + 1] = list()

    for i in range(m):  # 간선의 수만큼 정점 넣어주기
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for value in graph.values(): # 내림차순 방문
        value.sort(reverse=True)

    dfs(r)

    for o in range(1, len(visited)):
        print(visited[o])