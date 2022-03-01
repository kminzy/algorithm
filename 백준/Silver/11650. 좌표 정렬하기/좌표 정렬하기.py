import sys

n = int(sys.stdin.readline().rstrip())
matrix = []

for i in range(n):
    pos = tuple(map(int, sys.stdin.readline().split()))

    matrix.append(pos)

matrix = sorted(matrix, key=lambda x: (x[0], x[1]))

for i in matrix:
    print(i[0], i[1])