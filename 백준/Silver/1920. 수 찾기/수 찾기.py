import sys

N = int(sys.stdin.readline().rstrip())
N_list = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    print(1) if i in N_list else print(0)