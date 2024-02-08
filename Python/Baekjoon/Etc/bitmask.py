# https://www.acmicpc.net/problem/11723

import sys

def main():
    input_ = sys.stdin.readline
    n = int(input_())
    current = 0
    for _ in range(n):
        commands = input_().split()
        operation = commands[0]
        if len(commands) ==1:
            match operation:
                    case 'all':
                        current = (1<<21)-1
                    case 'empty':
                        current = 0
        else:
            mask = 1<<int(commands[1])
            match operation:
                case 'add':
                    current |= mask
                case 'remove':
                    current &= ~mask
                case 'check':
                    if current & mask == 0:
                        print(0)
                    else:
                        print(1)
                case 'toggle':
                    current ^= mask
                        
if __name__ == '__main__':
    main()
