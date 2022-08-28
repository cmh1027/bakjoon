import sys
input = sys.stdin.readline
N = int(input())
RB = [-1 for _ in range(N)]
stack = []
L = list(map(int, input().split()))
for i, num in enumerate(L):
    if len(stack) == 0:
        stack.append((i, num))
    else:
        while len(stack) > 0:
            top_i, top_num = stack[-1]
            if top_num >= num:
                break
            RB[top_i] = num
            stack.pop()
        stack.append((i, num))
print(*RB)