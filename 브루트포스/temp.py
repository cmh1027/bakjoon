import sys
input = sys.stdin.readline
x = int(input())
y = list(range(10))
count = 0
while count <= x and len(y) > 0:
    # [9876543210]
    k = y.pop(0)
    one = k % 10
    for i in range(one):
        y.append(k * 10 + i)
    count += 1
if count <= x:
    print(-1)
else:
    print(k)