# https://www.acmicpc.net/problem/11723

import sys

class Set:

    def __init__(self):
        self.current = 0
        self.power_two = [0, *map(lambda x: 2**x, range(21))]
    
    def add(self, x):
        self.current = self.current | self.power_two[x]
    
    def remove(self, x):
        self.current = self.current & ~self.power_two[x]
    
    def check(self, x):
        return (self.current & self.power_two[x]) >> x-1
    
    def toggle(self, x):
        self.current = self.current ^ self.power_two[x]
    
    def all(self):
        self.current = self.power_two[21]-1
    
    def empty(self):
        self.current = 0

def main():
    input_ = sys.stdin.readline
    n = int(input_())

    set_ = Set()
    for _ in range(n):
        commands = input_().split()
        operation = commands[0]
        if len(commands) == 1:
            getattr(set_, operation)()
        else:
            x = int(commands[1])
            if operation == 'check':
                print(set_.check(x))
            else:
                getattr(set_, operation)(x)

            
if __name__ == '__main__':
    main()
