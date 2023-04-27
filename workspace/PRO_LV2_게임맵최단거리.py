from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    wallMaps = getWall(maps, n, m)

    queue = deque()
    visited = []
    x, y, k = 1, 1, 1
    if (x, y) not in visited:
        queue.append((x, y, k))

        while queue:
            i, j, k = queue.popleft()
            if i > n and j > m:
                return -1
            tuple = getTuple(i, j, k)
            for tx, ty, tk in tuple:
                if tx == n and ty == m:
                    return tk
                if wallMaps[tx][ty] == 1 and (tx, ty) not in visited:
                    queue.append((tx, ty, tk))
                    visited.append((tx, ty, tk))

def getWall(maps, x, y):
    arr = [[0] * (x + 2) for _ in range(y + 2)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            arr[i][j] = maps[i - 1][j - 1]

    return arr

def getTuple(x, y, k):
    return (x + 1, y, k + 1), (x, y + 1, k + 1), (x - 1, y, k + 1), (x, y - 1, k + 1)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))