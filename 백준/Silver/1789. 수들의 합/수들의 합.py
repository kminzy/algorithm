s = int(input())

total = 0
cnt = -1

for i in range(1, 4294967295):
    total += i
    cnt += 1

    if total > s:
        break

print(cnt)