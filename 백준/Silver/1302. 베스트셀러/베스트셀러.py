import sys

n = int(sys.stdin.readline().rstrip())
books = dict()

for i in range(n):
    book = sys.stdin.readline().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

books = dict(sorted(books.items(), key=lambda x: x[0]))

maxCount = max(books.values())

for key, value in books.items():
    if value == maxCount:
        print(key)
        break
