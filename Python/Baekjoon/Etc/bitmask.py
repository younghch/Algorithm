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
            x = int(commands[1])
            match operation:
                case 'add':
                    current |= 1<<x
                case 'remove':
                    current &= ~(1<<x)
                case 'check':
                    if current & (1<<x) == 0:
                        print(0)
                    else:
                        print(1)
                case 'toggle':
                    current ^= 1<<x
                        
if __name__ == '__main__':
    main()
