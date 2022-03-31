import sys

N = int(sys.stdin.readline().rstrip())
house = list(map(int, sys.stdin.readline().split()))
house.sort()

print(house[(N - 1) // 2])