import sys
input = sys.stdin.readline
N = int(input())
A, B = map(int, input().split())
C = int(input())
topping = []
for _ in range(N):
    topping.append(int(input()))
topping.sort(reverse=True)
calSum = C
priceSum = A
maxCal = int(C/A)
for index, cal in enumerate(topping):
    calSum, priceSum = calSum + cal, priceSum + B
    if maxCal < int(calSum / priceSum):
        maxCal = int(calSum / priceSum)
print(maxCal)