import sys
input = sys.stdin.readline
Z = int(input())
y = Z // 5
while y >= 0:
    if (Z - 5 * y) % 3 == 0:
        print((Z - 5 * y) // 3+y)
        break
    y -= 1
else:
    print(-1)