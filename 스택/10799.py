import sys
input = sys.stdin.readline
S = input().strip()
stack = [S[0]]
pieces = 0
for i in range(1, len(S)):
    if S[i] != ')':
        stack.append(S[i])
    else:
        stack.pop() 
        if S[i-1] == '(': # laser
            pieces += len(stack)
        else:
            pieces += 1
print(pieces)
