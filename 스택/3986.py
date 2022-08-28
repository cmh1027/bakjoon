import sys
input = sys.stdin.readline
N = int(input())
number = 0
for _ in range(N):
    stack = []
    S = input().strip()
    for c in S:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        number = number + 1
print(number)