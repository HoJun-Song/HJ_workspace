from collections import deque

def solution(n, computers):
    answer = 0

    queue = deque()
    visited = []
    for x in range(n):
        if x not in visited:
            queue.append(x)
            answer += 1

            while queue:
                moveX = queue.popleft()
                for i in range(n):
                    if computers[moveX][i] == 1 and i not in visited:
                        queue.append(i)
                        visited.append(i)

    print(visited)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

"""
BFS
"""
def bfs(computers, start, visited):
    queue = deque([start])
    visited = [start]
    while queue:
        v = queue.popleft()
        for i in computers[v]:
            if i not in visited:
                queue.append(i)
            visited.append(i)
    return visited

"""
DFS
"""
def dfs(graph, x, visited):
    visited += [x]
    for i in graph[x]:
        if i not in visited:
            dfs(graph, i, visited)