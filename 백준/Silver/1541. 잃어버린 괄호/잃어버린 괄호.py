import sys

s = sys.stdin.readline().rstrip()

minus = s.split('-')

result = []

for i in range(len(minus)):
    plus = list(map(int, minus[i].split('+')))
    result.append(sum(plus))

answer = result[0]

if len(result) > 1:
    for i in range(1, len(result)):
        answer -= result[i]

print(answer)