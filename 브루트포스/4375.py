# (A + B) % N = (A % N + B % N) % N
# (A ∗ B) % N = (A % N) ∗ (B % N) % N
# (A + 1) % N = (A % N + 1) % N
# (A * 10 + 1) % N = (A * 10 % N + 1) % N = ((A % N) * (10 % N) % N + 1) % N
# 11 % N = (1 * 10 + 1) % N = ((1 % N) * (10 % N) % N + 1) % N
# 111 % N = (11 * 10 + 1) % N = ((11 % N) * (10 % N) % N + 1) % N

import sys
lines = sys.stdin.readlines()
for line in lines:
    N = int(line)
    c = 1
    m = 1
    if N == 1:
        print(1)
        continue
    while m != 0:
        m = ((m % N) * (10 % N) % N + 1) % N
        c = c + 1
    print(c)