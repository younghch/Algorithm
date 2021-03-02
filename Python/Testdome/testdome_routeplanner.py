""""
As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.

The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present or False if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if it is not. The from_row and from_column parameters are the starting row and column in the map_matrix. The to_row and to_column are the destination row and column in the map_matrix. The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return True since the destination is reachable:
"""


def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    visited = list()
    x_max = len(map_matrix)
    y_max = len(map_matrix[0])
    for i in range(x_max):
        visited.append([])
        for j in range(y_max):
            visited[i].append(False)
    visited[from_row][from_column] = True
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(x, y):
        if (x, y) == (to_row, to_column):
            return True
        for move in moves:
            x_next, y_next = x + move[0], y + move[1]
            if 0 <= x_next < x_max and 0 <= y_next < y_max and not visited[x_next][y_next] and map_matrix[x_next][y_next]:
                visited[x_next][y_next] = True
                if dfs(x_next, y_next) is True:
                    return True
                visited[x_next][y_next] = False
        return False
    return dfs(from_row, from_column)


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [False, False, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
