import sys
from itertools import combinations
input = sys.stdin.readline
N, K = map(int, input().split())
maximum = 0
first_words = {'a', 'n', 't', 'i', 'c'}
if K < 5:
    print(0)
else:
    words = []
    for _ in range(N):
        words.append(set(input().strip()))
    alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
    for c in first_words:
        alphabet.remove(c)
    learned = [0] * (ord('z') + 1)
    for c in first_words:
        learned[ord(c)] = 1
    for comb in combinations(alphabet, K-5):
        for c in comb:
            learned[ord(c)] = 1
        readable = 0
        for word in words:
            for i in word:
                if learned[ord(i)] == 0:
                    break
            else:
                readable += 1
        maximum = max(readable, maximum)
        for c in comb:
            learned[ord(c)] = 0
    print(maximum)               
    