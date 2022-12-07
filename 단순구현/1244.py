import sys
input = sys.stdin.readline
T = int(input())
switch = [-1] + list(map(int, input().split()))
N = int(input())
for _ in range(N):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, T+1, num):
            switch[i] = (switch[i] + 1) % 2
    else:
        j = 0
        while num - j > 0 and num + j <= T and switch[num-j] == switch[num+j]:
            j = j + 1
        j = j - 1
        for i in range(num-j, num+j+1):
            switch[i] = (switch[i] + 1) % 2
switch = switch[1:]
for i in range(0, len(switch), 20):
    print(*switch[i:i+20])