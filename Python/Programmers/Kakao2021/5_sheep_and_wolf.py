'''
https://programmers.co.kr/learn/courses/30/lessons/92343
'''
from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

def solution(info, edges):
    global max_num_of_sheep
    
    max_num_of_sheep = 0
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
    
    def dfs(cur, candidates, count_sheep, count_wolf):
        global max_num_of_sheep
        count_sheep += info[cur]^1
        count_wolf += info[cur]
        if count_sheep > count_wolf:
            if count_sheep > max_num_of_sheep:
                max_num_of_sheep = count_sheep
            next_candidates = candidates + tree[cur]
            for next_ in next_candidates:
                dfs(next_, [x for x in next_candidates if x != next_],count_sheep, count_wolf)

    dfs(0, [], 0, 0)
    return max_num_of_sheep
