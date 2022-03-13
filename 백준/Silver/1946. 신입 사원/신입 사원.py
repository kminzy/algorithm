import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    score = []

    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())  # [서류 순위, 면접 순위]
        score.append([a, b])

    score = sorted(score, key=lambda score: score[0])  # 서류 순위를 바탕으로 sort

    count = 1 # 첫 번째 사람은 무조건 pick
    standard = score[0][1] # 기준이 되는 첫 번째 사람의 면접 순위

    for i in range(1, len(score)):
        if score[i][1] < standard:
            count += 1
            standard = score[i][1] # 기준을 갱신

    print(count)