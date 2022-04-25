import sys

input_ = sys.stdin.readline

t = int(input_())

def get_ink_status(cartridges):
    colors = []
    sum_ = 0

    for i in range(4):
        if sum_ == 10**6:
            colors.append(0)
            continue
        min_ink = float('inf')
        for j in range(3):
            min_ink = min(min_ink, cartridges[j][i])
        if sum_+min_ink <= 10**6:
            colors.append(min_ink)
            sum_ += min_ink
        else:
            colors.append(10**6-sum_)
            sum_ = 10**6
    if sum_ != 10**6:
        return ['IMPOSSIBLE']
    return colors


for i in range(t):
    cartridges = [tuple(map(int, input_().split())) for _ in range(3)]
    print(f'Case #{i+1}:', *get_ink_status(cartridges))
