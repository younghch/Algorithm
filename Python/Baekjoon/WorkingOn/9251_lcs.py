'''
https://www.acmicpc.net/problem/9251
'''
import sys
from collections import defaultdict

input_ = sys.stdin.readline

s1 = input_().rstrip()
s2 = input_().rstrip()

lcs = [(-1)]*(len(s1)+1)
len_ = 1
s1_idxes = defaultdict(list)

for idx, c in enumerate(s1):
    s1_idxes[c].append(idx)

for c in s2:
    idxes = s1_idxes[c]
    for i in range(1, len_):
        for idx in idxes:
            if lcs[i-1] != idx and lcs[i-1] < idx and idx < lcs[i]:
                lcs[i] = idx
                break
    for idx in idxes:
        if idx > lcs[len_-1]:
            lcs[len_] = idx
            len_ += 1
            break

print(len_-1)
