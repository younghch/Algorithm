'''
https://www.acmicpc.net/problem/7568
'''

import sys

def getNumberOfLarger(me, whole):
    count = 0
    for p in whole:
        if me[0] < p[0] and me[1] < p[1]:
            count += 1
    return count


def main():
    n = int(sys.stdin.readline())
    whole = []
    for _ in range(n):
        whole.append(list(map(int, sys.stdin.readline().split())))
    score = []
    for p in whole:
        score.append(getNumberOfLarger(p, whole) + 1)
    print(*score)

main()
