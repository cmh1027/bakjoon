import sys
input = sys.stdin.readline
N = int(input())
square = [0, 0, 0]
score = [0, 0, 0]
for _ in range(N):
    A, B, C = map(int, input().split())
    square[0] += A ** 2
    score[0] += A
    square[1] += B ** 2
    score[1] += B
    square[2] += C ** 2
    score[2] += C
square = list(enumerate(square))
square.sort(key=lambda x:x[1], reverse=True)
if square[0][1] == square[1][1]:
    print(0, score[square[0][0]])
else:
    print(square[0][0]+1, score[square[0][0]])