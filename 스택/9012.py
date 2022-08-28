import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    stack = []
    S = input().strip()
    for c in S:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                print("NO")
                break
            stack.pop()
    else:
        if len(stack) != 0:
            print('NO')
        else:
            print('YES')
