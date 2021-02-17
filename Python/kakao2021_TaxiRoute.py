"""
[문제]
지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다. 이때, A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성해 주세요.
만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.

[제한사항]
지점갯수 n은 3 이상 200 이하인 자연수입니다.
지점 s, a, b는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.
즉, 출발지점, A의 도착지점, B의 도착지점은 서로 겹치지 않습니다.
fares는 2차원 정수 배열입니다.
fares 배열의 크기는 2 이상 n x (n-1) / 2 이하입니다.
예를들어, n = 6이라면 fares 배열의 크기는 2 이상 15 이하입니다. (6 x 5 / 2 = 15)
fares 배열의 각 행은 [c, d, f] 형태입니다.
c지점과 d지점 사이의 예상 택시요금이 f원이라는 뜻입니다.
지점 c, d는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.
요금 f는 1 이상 100,000 이하인 자연수입니다.
fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다.
출발지점 s에서 도착지점 a와 b로 가는 경로가 존재하는 경우만 입력으로 주어집니다.

"""
import collections
import heapq


def solution(n, s, a, b, fares):
    answer = float("inf")
    graph = collections.defaultdict(list)

    # initialize graph
    for i, j, f in fares:
        graph[i].append((f, j))
        graph[j].append((f, i))

    # calculate cost of each vertex when moving together using bfs
    v_weights = collections.defaultdict(lambda: float("inf"))
    v_weights[s] = 0

    queue = [(0, s)]
    while queue:
        cur_cost, cur_v = heapq.heappop(queue)
        for cost, next_v in graph[cur_v]:
            if cur_cost + cost < v_weights[next_v]:
                v_weights[next_v] = cur_cost + cost
                heapq.heappush(queue, (v_weights[next_v], next_v))
    print(v_weights)

    # calculate the sum of costs to A, B for each vertex
    def calc_cost(v_s, v_a, v_b):
        temp_weights = collections.defaultdict(lambda: float("inf"))
        temp_weights[v_s] = 0
        temp_queue = [(0, v_s)]
        while temp_queue:
            temp_cur_cost, temp_cur = heapq.heappop(temp_queue)
            for next_cost, temp_next in graph[temp_cur]:
                if temp_cur_cost + next_cost <  temp_weights[temp_next]:
                    temp_weights[temp_next] = temp_cur_cost + next_cost
                    heapq.heappush(temp_queue, (temp_weights[temp_next], temp_next))
        return v_weights[v_s] + temp_weights[v_a] + temp_weights[v_b]
    for i in range(1, n + 1):
        answer = min(calc_cost(i, a, b), answer)
    return answer


def solution2(n, s, a, b, fares):
    d = [[20000001 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv


print(solution(6, 4, 6, 2, 	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
