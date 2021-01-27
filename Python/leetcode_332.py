from typing import *
import collections

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dic = collections.defaultdict(list)
        # for ticket in sorted(tickets):
        #     dic[ticket[0]].append(ticket[1])
        # if dic["JFK"] is None:
        #     return []
        # result = []
        #
        # def dfs(cur):
        #     while dic[cur]:
        #         dfs(dic[cur].pop(0))
        #         result.append(cur)
        # dfs("JFK")
        # return result[::-1]

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append((b))

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append((graph[stack[-1]].pop()))
            route.append(stack.pop())

        return route[::-1]


s = Solution()
print(s.findItinerary([["JFK","AAA"],["JFK","ATL"],["AAA","ATL"],["ATL","JFK"],["ATL","AAA"]]))
