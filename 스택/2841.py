import sys
input = sys.stdin.readline
N, P = map(int, input().split())
stacks = [[] for _ in range(7)]
count = 0
for _ in range(N):
    string, fret = map(int, input().split())
    stack = stacks[string]
    if len(stack) == 0:
        stack.append(fret)
        count = count + 1
    else:
        while len(stack) > 0 and stack[-1] > fret:
            stack.pop()
            count = count + 1
        if len(stack) == 0 or len(stack) > 0 and stack[-1] < fret:
            stack.append(fret)
            count = count + 1
print(count)