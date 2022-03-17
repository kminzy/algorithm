import sys

E, S, M = map(int, sys.stdin.readline().split())
ez, sz, mz, cnt = 1, 1, 1, 1

while True:
    if ez == E and sz == S and mz == M:
        print(cnt)
        break

    cnt += 1
    ez += 1
    sz += 1
    mz += 1

    if ez > 15:
        ez -= 15
    if sz > 28:
        sz -= 28
    if mz > 19:
        mz -= 19