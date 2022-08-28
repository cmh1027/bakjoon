import sys
input = sys.stdin.readline
S = input().strip()
count = [-1] * (ord('z') - ord('a') + 1)
for i, c in enumerate(S):
    if count[ord(c) - ord('a')] == -1:
        count[ord(c) - ord('a')] = i
print(*count)