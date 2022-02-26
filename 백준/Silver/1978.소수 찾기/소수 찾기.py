import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().split()))
result = []

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in n_list:
    result.append(isPrime(i))

print(result.count(True))