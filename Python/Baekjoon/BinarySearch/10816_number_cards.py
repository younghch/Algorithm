'''
https://www.acmicpc.net/problem/10816
Of course, using a hashmap is faster. Used binary search to practice
'''
import sys

input_ = sys.stdin.readline

n = int(input_())
numbers = sorted(map(int, input_().split()))
m = int(input_())
targets = map(int, input_().split())
ans = []

def get_left_idx(left, right, target):
    if left > right:
        if left == n or numbers[left] != target:
            return -1
        return left
    mid = (left+right)//2
    if target <= numbers[mid]:
        return get_left_idx(left, mid-1, target)
    else:
        return get_left_idx(mid+1, right, target)

def get_right_idx(left, right, target):
    if left > right:
        if right == -1 or numbers[right] != target:
            return -1
        return right
    mid = (left+right)//2
    if target < numbers[mid]:
        return get_right_idx(left, mid-1, target)
    else:
        return get_right_idx(mid+1, right, target)

for target in targets:
    l = get_left_idx(0, n-1, target)
    if l == -1:
        ans.append('0')
        continue
    r = get_right_idx(0, n-1, target)
    ans.append(str(r-l+1))

print(' '.join(ans))

