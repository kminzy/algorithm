import sys

N = int(sys.stdin.readline().rstrip())
students = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
total = 0


def counting(target):
    global students, total, count

    count = 0

    if target - B <= 0:
        count += 1
    else:
        now = target - B
        count += 1  # 총감독관 1명 더해줌
        count += (now // C)  # 부감독관 필요한만큼 더해줌
        now2 = (now % C)
        if now2 >= C:
            counting(C)
        elif now2 == 0:
            count += 0
        else:
            count += 1


for i in range(len(students)):
    counting(students[i])
    total += count

print(total)
