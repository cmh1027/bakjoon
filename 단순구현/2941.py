import sys
input = sys.stdin.readline
L = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = input().strip()
count = 0
for i in L:
    count = count + S.count(i)
    S = S.replace(i, " ")
count = count + len(S) - S.count(" ")
print(count)