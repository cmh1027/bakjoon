import sys
input = sys.stdin.readline
T = int(input())
def check(S):
    appear = {S[0]}
    current = S[0]
    for c in S[1:]:
        if c != current:
            if c in appear:
                return False
            else:
                appear.add(c)
                current = c
    return True
count = 0
for _ in range(T):
    S = input().strip()
    if check(S) is True:
        count = count + 1
print(count)