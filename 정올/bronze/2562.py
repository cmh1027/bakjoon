import sys
input = sys.stdin.readline
num = []
for _ in range(9):
    num.append(int(input()))
M = -1
index = -1
for i in range(9):
    if M < num[i]:
        index = i
        M = num[i]
print(M)
print(index+1)