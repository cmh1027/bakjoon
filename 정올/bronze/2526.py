import sys
input = sys.stdin.readline
N, P = map(int, input().split())
A = [-1] * 100000
current = N
while True:
    next = (current * N) % P
    A[current] = next
    if A[next] != -1:
        start = next
        break
    current = next
node = start
count = 1
while True:
    node = A[node]
    if node == start:
        break
    count = count + 1
print(count)