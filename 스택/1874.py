import sys
input = sys.stdin.readline
N = int(input())
stack = []
L = []
result = []
for _ in range(N):
    L.append(int(input()))
for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    while len(L) > 0 and len(stack) > 0 and L[0] == stack[-1]:
        L.pop(0)
        stack.pop()
        result.append('-')
if len(L) > 0:
    print("NO")
else:
    for i in result:
        print(i)