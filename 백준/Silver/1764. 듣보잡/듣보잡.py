import sys

n, m = map(int, sys.stdin.readline().split())
names1 = set()
names2 = set()

for _ in range(n):
    name1 = sys.stdin.readline().rstrip()
    names1.add(name1)

for _ in range(m):
    name2 = sys.stdin.readline().rstrip()
    names2.add(name2)

answer = sorted(list(names1 & names2))

print(len(answer))

for i in answer:
    print(i)