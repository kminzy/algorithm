import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return 0


n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 오름차순 정렬
sorted_numbers = sorted(numbers)

d = dict()  # 결과를 담을 딕셔너리

for i in range(len(cards)):
    if cards[i] in d:
        d[cards[i]] += binary_search(sorted_numbers, cards[i], 0, m - 1)
    else:
        d[cards[i]] = binary_search(sorted_numbers, cards[i], 0, m - 1)

result = []

for number in numbers:
    if number in d:
        result.append(str(d[number]))
    else:
        result.append(str(0))

print(' '.join(result))