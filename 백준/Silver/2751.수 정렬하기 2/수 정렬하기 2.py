import sys

n = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for n in numbers:
    print(n)