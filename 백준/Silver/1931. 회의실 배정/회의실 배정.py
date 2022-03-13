import sys

n = int(sys.stdin.readline().rstrip())
times = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    times.append([start, end])

times = sorted(times, key=lambda x: (x[1], x[0]))

cnt = 1
end_time = times[0][1]

for i in range(1, len(times)):
    if times[i][0] >= end_time:
        cnt += 1
        end_time = times[i][1]

print(cnt)