import sys

trees = dict()

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

trees = dict(sorted(trees.items(), key=lambda x:x[0]))

total = sum(trees.values())

for key, value in trees.items():
    print(key, '%.4f' % (value / total * 100))