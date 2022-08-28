# import sys
# def fibo(N):
#     L = [0, 1, 1]
#     a, b = 1, 1
#     for _ in range(2, N):
#         a, b = b, a + b
#         L.append(b)
#     return L
# input = sys.stdin.readline
# D, K = map(int, input().split())
# fibolist = fibo(D)
# for i in range(1, K):
#     if (K - fibolist[D-2] * i) % fibolist[D-1] == 0:
#         print(i)
#         print((K - fibolist[D-2] * i) // fibolist[D-1])
#         exit(0)

import sys
input=sys.stdin.readline
a,b=map(int, input().split())
L = [0 for _ in range(a+1)]
L[1] = 1
L[2] = 1
def fibonacci(a):
    if L[a] != 0:
        return L[a]
    else:
        L[a] = fibonacci(a-1) + fibonacci(a-2)
        return L[a]
for A in range(1, b):
    if (b-fibonacci(a-2)*A)%fibonacci(a-1)==0:
        k=(b-fibonacci(a-2)*A)/fibonacci(a-1)
        print(A)
        print(int(k))
        break 
