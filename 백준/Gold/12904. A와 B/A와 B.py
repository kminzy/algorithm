import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

flag = False

while len(S) <= len(T):
    if S != T:
        if T[-1] == 'A':
            T = T[:-1]
        elif T[-1] == 'B':
            T = T[:-1]
            T = T[::-1]
    else:
        flag = True
        break

if flag == True:
    print(1)
else:
    print(0)

# S에서 T로 만드는 방식으로 구현하면 메모리 초과 오류
# 역으로 T에서 S를 만드는 방식으로 구현