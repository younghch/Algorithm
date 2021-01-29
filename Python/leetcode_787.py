"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
"""

from typing import *
import collections
import heapq


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))
        queue = [(0, -1, src)]  # (cost, depth, node)
        while queue:
            cur = heapq.heappop(queue)
            if cur[2] == dst:
                return cur[0]
            if cur[1] == K:
                continue
            for nex, cost in graph[cur[2]]:
                heapq.heappush(queue, (cur[0] + cost, cur[1] + 1, nex))
        return -1


s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
