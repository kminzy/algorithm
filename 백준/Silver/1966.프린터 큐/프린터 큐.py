import sys

testcase = int(sys.stdin.readline().rstrip())

for i in range(testcase):
    n, m = map(int, sys.stdin.readline().split())
    document = list(map(int, sys.stdin.readline().split()))
    chk = [0 for _ in range(n)]
    chk[m] = 1 # target
    cnt = 0

    while document:
        if document[0] == max(document):
            cnt += 1
            if chk[0] == 1:
                print(cnt)
                break
            else:
                chk.pop(0)
                document.pop(0)
        else:
            chk.append(chk.pop(0))
            document.append(document.pop(0))