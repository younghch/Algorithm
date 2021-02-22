"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

"""

'''
:param W: capacity of knapsack 
:param wt: list containing weights
:param val: list containing corresponding values
:param n: size of lists
:return: Integer
'''


def knapSack(W, wt, val, n):
    table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if w < wt[i - 1]:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w - wt[i - 1]] + val[i - 1], table[i - 1][w])
    return table[n][W]


print(knapSack(15, [12, 1, 4, 1], [4, 2, 10, 1], 4))
