import sys
import math
input = sys.stdin.readline
def reduction(a, b):
    return a // math.gcd(a, b), b // math.gcd(a, b)
N = int(input())
L = list(map(int, input().split()))
a, b = 1, 1
for i in range(N-1):
    a, b = a * L[i], b * L[i+1]
    a, b = reduction(a, b)
    print(f"{a}/{b}")