'''
https://www.acmicpc.net/problem/1450
'''
import sys
# from bisect import bisect_right


input_ = sys.stdin.readline
n, c = map(int, input_().split())
weights = list(map(int, input_().split()))

right_half = [0]
left_half = [0]

for i in range(n//2):
    for j in range(len(right_half)):
        sum_ = weights[i]+right_half[j]
        if (sum_ <= c):
            right_half.append(sum_)
for i in range(n//2, n):
    for j in range(len(left_half)):
        sum_ = weights[i]+left_half[j]
        if (sum_ <= c):
            left_half.append(sum_)

right_half.sort()

def binary_search(left, right, val):
    while left <= right:
        mid = (left+right)//2
        # left + val > c return left
        # left + val <= c return left+1
        if right_half[mid]+val > c:
            right = mid-1
        else:
            left = mid+1
    return left

ans = 0
for v in left_half:
    ans += binary_search(0, len(right_half)-1, v)
    # ans += bisect_right(right_half, c-v)

print(ans)
                        