'''
https://www.acmicpc.net/problem/2493
'''
import sys

input_ = sys.stdin.readline

n = int(input_())
towers = list(enumerate(map(int, input_().split())))
stack = [towers.pop()]
ans = [0]*n

while towers:
    receive_loc, receive_height = towers.pop()
    while stack and stack[-1][1] < receive_height:
        send_loc, send_height = stack.pop()
        ans[send_loc] = receive_loc+1
    stack.append((receive_loc, receive_height))

print(*ans)
