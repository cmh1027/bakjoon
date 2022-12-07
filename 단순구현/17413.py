import sys
input = sys.stdin.readline
S = list(input().strip())
isTag = False
start = 0
for i in range(len(S)):
    if S[i] == '<':
        isTag = True
        S[start:i] = list(reversed(S[start:i]))
    if S[i] == '>':
        isTag = False
        start = i+1
    if S[i] == ' ' and isTag is False:
        S[start:i] = list(reversed(S[start:i]))
        start = i+1
S[start:] = list(reversed(S[start:]))
print(''.join(S))