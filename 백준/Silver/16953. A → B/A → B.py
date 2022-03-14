import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())


def bfs():
    queue = deque([(A, 1)])  # [target, cnt]

    while queue:
        target, cnt = queue.popleft()  # 꺼내기

        if target == B:
            return cnt

        if target * 2 <= B:
            queue.append((target * 2, cnt + 1))

        if int(str(target) + '1') <= B:
            queue.append((int(str(target) + '1'), cnt + 1))

    return -1  # 만들 수 없는 경우


print(bfs())

# cnt를 따로 빼서 풀었더니 2배 연산과 1 더하기 연산에서 모두 cnt 횟수가 증가함
# queue의 요소로 target과 cnt를 묶어서 연산 => 해결