import sys
import itertools
input = sys.stdin.readline
N = int(input())
perm = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
for _ in range(N):
    X, strike, ball = input().strip().split()
    strike, ball = int(strike), int(ball)
    X = tuple(map(int, X))
    for i in range(len(perm)-1, -1, -1):
        strike_num, ball_num = 0, 0
        for j in range(3):
            if X[j] in perm[i]:
                if X[j] != perm[i][j]:
                    ball_num += 1
                else:
                    strike_num += 1
        if strike != strike_num or ball != ball_num:
            del perm[i]
print(len(perm))