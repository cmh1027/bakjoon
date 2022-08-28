# pypy말고 python으로 제출하면 시간초과
import sys
input = sys.stdin.readline
L, C = map(int, input().split())
candidate = list(input().strip().split())
candidate.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}
result = []
def recursion(index, consonant, vowel, string):
    global L, candidate, vowels, result
    if len(string) + (len(candidate) - index) < L:
        return
    if index == C or len(string) == L:
        if consonant >= 2 and vowel >= 1 and len(string) == L:
            result.append(string)
        return
    c = candidate[index]
    if c in vowels:
        recursion(index+1, consonant, vowel+1, string+c)
    else:
        recursion(index+1, consonant+1, vowel, string+c)
    recursion(index+1, consonant, vowel, string)
recursion(0, 0, 0, "")
for string in result:
    print(string)