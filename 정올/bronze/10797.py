import sys
input = sys.stdin.readline
A = int(input())
L = list(map(int, input().split()))
count = 0
for num in L:
    if num % 10 == A:
        count += 1
print(count)