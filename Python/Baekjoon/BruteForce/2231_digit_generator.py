'''
https://www.acmicpc.net/source/38558968
'''
import sys

def getMinGenerator(n, power):
    if n < 0:
        return -1
    if power == 0:
        return 0 if n == 0 else -1

    for i in range(10):
        subGenerator = getMinGenerator(n-(power+1)*i, power//10)
        if subGenerator != -1:
            return power*i+subGenerator
    return -1


def main():
    n = sys.stdin.readline().strip()
    ans = getMinGenerator(int(n), 10**(len(n)-1))
    if ans == -1:
        print(0)
    else:
        print(ans)

main()
