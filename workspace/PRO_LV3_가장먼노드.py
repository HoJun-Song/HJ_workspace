import heapq
INF = 10*9
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,[0,start])

    while q:
        # print(q)
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for n,c in graph[now]:
            cost = c + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q,[cost,n])
        # print(distance)
    return max(distance[1:])

def solution(n, edge):
    global graph, distance
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for e in edge:
        graph[e[0]].append([e[1],1])
        graph[e[1]].append([e[0],1])
    for g in graph:
        g.sort()
    # print(graph)
    m = dijkstra(1)
    return distance.count(m)

"""
다익스트라 알고리즘! 그래프 최단경로
"""


"""
BFS 이어져 있는 노드를 계층 구조처럼 표현
"""
from collections import deque


def solution(n, edge):
    maps = [[] for _ in range(n)]
    for e in edge:
        maps[e[0] - 1].append([e[1] - 1, 1])
        maps[e[1] - 1].append([e[0] - 1, 1])

    visited = [0] * n
    answer = bfs(maps, 0, visited)
    return visited.count(answer)


def bfs(maps, v, visited):
    q = deque()
    q.append(v)
    visited[v] = 0
    while q:
        node = q.popleft()

        recentNode = maps[node]
        for i in recentNode:
            if visited[i[0]] == 0:
                visited[i[0]] = visited[node] + 1
                q.append(i[0])

    visited[0] = 0
    return max(visited)