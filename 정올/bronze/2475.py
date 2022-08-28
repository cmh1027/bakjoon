import sys
input = sys.stdin.readline
L = list(map(int, input().split()))
print(sum(map(lambda x:x**2, L)) % 10)