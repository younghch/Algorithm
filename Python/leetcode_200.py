from typing import *
"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


def dfs(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
        return
    grid[row][col] = '0'

    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)


def numIslands(grid: List[List[str]]) -> int:
    print("function called")
    count = 0
    not_all_zero = True
    while not_all_zero:
        not_all_zero = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(grid, row, col)
    print(grid)
    return count


print(numIslands( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))