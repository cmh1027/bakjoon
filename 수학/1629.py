import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
cache = {}
def func(a, b, m):
    if b == 1:
        return a % m
    if b in cache:
        return cache[b]
    else:
        A = func(a, b//2, m)
        cache[b//2] = A
        if b % 2 == 0:
            return (A * A) % m
        else:
            return ((A * A % m) * (a % m)) % m

print(func(a, b, c))