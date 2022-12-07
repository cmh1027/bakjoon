import sys
input = sys.stdin.readline
doc = input().strip()
word = input().strip()
i = 0
count = 0
doclen = len(doc)
wordlen = len(word)
while i < doclen:
    if doc[i:i+wordlen] == word:
        count += 1
        i = i + wordlen
    else:
        i = i + 1
print(count)