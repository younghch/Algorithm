import sys

input_ = sys.stdin.readline

t = int(input_())
to_print = []

def get_press_count(products, dp):
    first_left, first_right = products[0]
    dp[0][0], dp[0][1] = first_right + first_right-first_left, first_right
    for i in range(1, len(products)):
        prev_left, prev_right = products[i-1]
        left, right = products[i]
        dist = right-left
        dp[i][0] = min(dp[i-1][0]+abs(prev_left-right), dp[i-1][1]+abs(prev_right-right))+dist
        dp[i][1] = min(dp[i-1][0]+abs(prev_left-left), dp[i-1][1]+abs(prev_right-left))+dist
    return min(dp[len(products)-1])

for i in range(t):
    n, _ = map(int, input_().split())
    dp = [[0, 0] for _ in range(n)]
    products = []
    for _ in range(n):
        cur = list(map(int, input_().split()))
        products.append((min(cur), max(cur)))
    to_print.append(f'Case #{i+1}: {get_press_count(products, dp)}')
    
print('\n'.join(to_print))
