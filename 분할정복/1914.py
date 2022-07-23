import sys

def hanoi(N, A, B, C): # N개의 현판을 A에서 B를 거쳐서 C로
    if(N == 1):
        print(A, C)
    else:
        hanoi(N-1, A, C, B)
        print(A, C)
        hanoi(N-1, B, A, C)

input = sys.stdin.readline
N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(N, 1, 2, 3)