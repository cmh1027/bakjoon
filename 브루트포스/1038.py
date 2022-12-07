import sys
input = sys.stdin.readline
N = int(input())
queue = list(range(10))
x = 0
while x <= N and len(queue) > 0:
    front = queue.pop(0)
    one = front % 10
    for i in range(one):
        queue.append(front * 10 + i)
    x = x + 1
if x <= N:
    print(-1)
else:
    print(front)