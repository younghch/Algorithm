'''
https://www.acmicpc.net/problem/13305
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
distances = list(map(int, input_().split()))
prices = list(map(int, input_().split()))
min_price = float('inf')
sum_ = 0

prices.pop()
for distance, price in zip(distances, prices):
    if min_price > price:
        min_price = price
    sum_ += min_price*distance

print(sum_)
