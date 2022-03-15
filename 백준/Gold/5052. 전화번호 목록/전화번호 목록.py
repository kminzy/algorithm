import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    num_list = []

    for i in range(n):
        number = sys.stdin.readline().rstrip()
        num_list.append(number)

    num_list = sorted(num_list)

    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i + 1][:len(num_list[i])]:  # 현재 번호가 다음 번호의 접두사?
            print("NO")
            break
    else:
        print("YES")