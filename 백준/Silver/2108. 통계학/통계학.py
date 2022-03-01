import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort()
cnt_num = Counter(numbers).most_common(2)

print(round(sum(numbers) / n))
print(numbers[n // 2])
#print(cnt_num)
if len(cnt_num) > 1:
    if cnt_num[0][1] == cnt_num[1][1]:
        print(cnt_num[1][0])
    else:
        print(cnt_num[0][0])
else:
    print(cnt_num[0][0])
print(max(numbers) - min(numbers))
