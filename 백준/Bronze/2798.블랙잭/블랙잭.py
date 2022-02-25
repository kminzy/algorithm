import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(len(cards)):
    a = cards[i]
    second_tmp = cards[cards.index(cards[i]) + 1:]
    for j in range(len(second_tmp)):
        b = second_tmp[j]
        third_tmp = second_tmp[second_tmp.index(second_tmp[j]) + 1:]
        for k in range(len(third_tmp)):
            c = third_tmp[k]
            answer.append(a + b + c)


answer = [l for l in answer if l <= m]
print(max(answer))