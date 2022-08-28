import sys
input = sys.stdin.readline
for _ in range(3):
    up = sum(list(map(int, input().split())))
    if up == 0:
        print('D')
    elif up == 1:
        print('C')
    elif up == 2:
        print('B')
    elif up == 3:
        print('A')
    else:
        print('E')