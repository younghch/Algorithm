'''
https://www.acmicpc.net/problem/10828
'''
import sys
input_ = sys.stdin.readline

n = int(input_())
stack = []

def operate_stack(command, num):
    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if len(stack) == 0 else 0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

for _ in range(n):
    commands = input_().split()
    if len(commands) == 2:
        operate_stack(commands[0], commands[1])
    else:
        operate_stack(commands[0], None)
