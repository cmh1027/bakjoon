import sys
input = sys.stdin.readline
S = input().strip()
current = S[0]
length = 10
for i in range(1, len(S)):
    if current != S[i]:
        length += 10
    else:
        length += 5
    current = S[i]
print(length)