import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, list(str(N))))
if sum(A) % 3 != 0:
    print(-1)
else:
    A.sort(reverse=True)
    if A[-1] != 0:
        print(-1)
    else:
        for i in A:
            print(i, end="")