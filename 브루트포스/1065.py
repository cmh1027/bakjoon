import sys
input = sys.stdin.readline
N = int(input())
count = 0
for i in range(1, N+1):
    s = str(i)
    if len(s) <= 2:
        count += 1
    else:
        for i in range(len(s)-2):
            if int(s[i+2]) - int(s[i+1]) != int(s[i+1]) - int(s[i]):
                break
        else:
            count += 1
print(count)