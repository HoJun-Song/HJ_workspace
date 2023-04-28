def findRoute(findOne, parentList):
    route = [findOne]
    while parentList[findOne]:
        pp = parentList[findOne]
        route.append(pp)
        parentList[findOne] = parentList[pp]

    return route

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)
    for i in range(N - 1):
        edge = list(map(int, input().split()))
        parent[edge[1]] = edge[0]
    x, y = map(int, input().split())

    routeX = findRoute(x, parent[:])
    routeY = findRoute(y, parent[:])

    lenX = len(routeX)
    lenY = len(routeY)
    if lenX >= lenY:
        for answer in routeY:
            if answer in routeX:
                print(answer)
                break
    else:
        for answer in routeX:
            if answer in routeY:
                print(answer)
                break

"""
트리에서 노드의 부모는 하나다.
"""