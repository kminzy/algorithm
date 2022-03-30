import sys

s = sys.stdin.readline().rstrip()

splitBy1 = [c for c in s.split('1') if c]
splitBy0 = [c for c in s.split('0') if c]

print(min(len(splitBy1), len(splitBy0)))