'''
https://www.acmicpc.net/problem/1436
'''
import sys

def main():
    n = int(sys.stdin.readline())
    i = 665
    count = 0
    while True:
        i += 1
        if '666' in str(i):
            count += 1
        if count == n:
            print(i)
            break

main()
