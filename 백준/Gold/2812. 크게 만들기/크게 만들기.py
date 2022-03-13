import sys

N, K = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().rstrip()))
result = []
cnt = 0

for i in range(N):
    while cnt <= K and result:
        if cnt == K:
            break
        if result[-1] < number[i]:  # 현재 값이 result의 마지막 값보다 클 때
            result.pop()
            cnt += 1
        else:
            break

    result.append(number[i])

for i in range(N - K):  # number가 내림차순으로 주어지는 경우, K개를 다 지우지 못할 수도 있다.
    print(result[i], end='')