# 1676
import sys
input = sys.stdin.readline
def twoCount(N):
    D = 2
    two = 0
    while D <= N:
        two += N // D
        D *= 2
    return two
def fiveCount(N):
    D = 5
    five = 0
    while D <= N:
        five += N // D
        D *= 5
    return five
n, m = map(int, input().split())
five = fiveCount(n) - fiveCount(m) - fiveCount(n-m)
two = twoCount(n) - twoCount(m) - twoCount(n-m)
print(min(five, two))