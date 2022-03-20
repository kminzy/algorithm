import sys

N = int(sys.stdin.readline().rstrip())
serialNums = []

for i in range(N):
    serial = sys.stdin.readline().rstrip()
    serialNums.append(serial)


def sumNumbers(arr):
    result = 0
    for i in arr:
        if i.isdigit():
            result += int(i)
    return result


answer = sorted(serialNums, key=lambda x: (len(x), sumNumbers(x), x))

for a in answer:
    print(a)