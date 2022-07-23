import heapq
import sys
input = sys.stdin.readline
N = int(input())
lectures = []
for _ in range(N):
    S, E = map(int, input().split())
    lectures.append((S,E))
lectures = sorted(lectures)
# lectures = sorted(lectures, key=lambda x:x[0])
queue = []
heapq.heappush(queue, lectures[0][1])
for i in range(1, N):
    if lectures[i][0] < queue[0]:
        heapq.heappush(queue, lectures[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, lectures[i][1])

print(len(queue))