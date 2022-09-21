'''
https://school.programmers.co.kr/learn/courses/30/lessons/49189?
'''
from collections import defaultdict


def bfs(n):
    cur_nodes = [1]
    all_visited = [True]*(n+1)
    ans = 0

    while visited != all_visited:
        next_nodes = []
        for cur_node in cur_nodes:
            for linked_nodes in graph[cur_node]:
                if not visited[linked_nodes]:
                    visited[linked_nodes] = True
                    next_nodes.append(linked_nodes)
        cur_nodes = next_nodes
        ans = len(next_nodes)
    return ans

def solution(n, edge):
    global visited, graph

    graph = defaultdict(list)
    visited = [False]*(n+1)
    visited[0] = True
    visited[1] = True
    

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    
    return bfs(n)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))