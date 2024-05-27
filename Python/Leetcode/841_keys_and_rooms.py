# https://leetcode.com/problems/keys-and-rooms
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        visited[0] = True
        keys = set(rooms[0])
        while keys:
            new_keys = set()
            for key in keys:
                if not visited[key]:
                    visited[key] = True
                    for new_key in rooms[key]:
                        if new_key not in keys and not visited[new_key]:
                            new_keys.add(new_key)
            keys = new_keys
        return all(visited)