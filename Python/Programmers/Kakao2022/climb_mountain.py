'''
https://school.programmers.co.kr/learn/courses/30/lessons/118669

2 ≤ n ≤ 50,000
n - 1 ≤ paths의 길이 ≤ 200,000
paths의 원소는 [i, j, w] 형태입니다.
i번 지점과 j번 지점을 연결하는 등산로가 있다는 뜻입니다.
w는 두 지점 사이를 이동하는 데 걸리는 시간입니다.
1 ≤ i < j ≤ n
1 ≤ w ≤ 10,000,000
서로 다른 두 지점을 직접 연결하는 등산로는 최대 1개입니다.
1 ≤ gates의 길이 ≤ n
1 ≤ gates의 원소 ≤ n
gates의 원소는 해당 지점이 출입구임을 나타냅니다.
1 ≤ summits의 길이 ≤ n
1 ≤ summits의 원소 ≤ n
summits의 원소는 해당 지점이 산봉우리임을 나타냅니다.
출입구이면서 동시에 산봉우리인 지점은 없습니다.
gates와 summits에 등장하지 않은 지점은 모두 쉼터입니다.
임의의 두 지점 사이에 이동 가능한 경로가 항상 존재합니다.
return 하는 배열은 [산봉우리의 번호, intensity의 최솟값] 순서여야 합니다.
'''

from heapq import heappush, heappop
from collections import defaultdict

def solution(n, paths, gates, summits):
    min_intensity = float('inf')
    min_summit = float('inf')
    graph = defaultdict(dict)

    gates = set(gates)
    summits = set(summits)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    for gate in gates:
        heap = [(0, gate)]
        visited = [False]*(n+1)
        local_intensity = 0
        while heap:
            intensity, cur = heappop(heap)
            local_intensity = max(intensity, local_intensity)
            visited[cur] = True

            if local_intensity > min_intensity:
                break
            if cur != gate and cur in summits:
                if min_intensity == local_intensity:
                    min_summit = min(min_summit, cur)
                if local_intensity < min_intensity:
                    min_intensity = local_intensity
                    min_summit = cur
            else:
                for next_, w in graph[cur]:
                    if not visited[next_] and next_ not in gates:
                        heappush(heap, (w, next_))
                        
    return [min_summit, min_intensity]

print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))