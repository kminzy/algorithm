import sys

N = int(sys.stdin.readline().rstrip())
T_list = []
P_list = []
answer = 0

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())
    T_list.append(T)
    P_list.append(P)


def counting(idx, profit):
    global answer

    if idx > N:  # N 초과하는 범위
        return
    if idx == N:
        answer = max(answer, profit)
        return
    if idx + T_list[idx] <= N:
        counting(idx + T_list[idx], profit + P_list[idx])
    counting(idx + 1, profit)


counting(0, 0)
print(answer)
