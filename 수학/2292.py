import sys
input = sys.stdin.readline
N = int(input())
n = 0
while True:
    if 6 * (n * (n+1)) // 2 + 1 >= N:
        print(n+1)
        break
    n += 1