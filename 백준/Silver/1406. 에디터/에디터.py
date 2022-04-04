import sys

string = sys.stdin.readline().rstrip()  # 문자열
m = int(sys.stdin.readline().rstrip())  # 명령 수

left = list(string)
right = []

for i in range(m):
    command = sys.stdin.readline().rstrip()
    if len(command) == 1:  # L, D, B
        if command == 'L':
            if len(left) > 0:
                right.append(left.pop())
        elif command == 'D':
            if len(right) > 0:
                left.append(right.pop())
        else:  # B
            if len(left) > 0:
                left.pop()
    else:  # P $
        c = command.split()
        left.append(c[1])

result = left + right[::-1]

print(''.join(result))