# 2022-07-12 1차시도 망
def solution(n, wires):
    minDiff = n
    for i in range(n):
        tmp = wires.pop(0)
        a, b = tmp[0], tmp[1]
        print(a, b)
        cntA = cntB = 0
        cpyWires = wires.copy()
        visit = []
        visit.append(cpyWires.pop(0))
        while len(cpyWires) > 0:
            cmp = cpyWires.pop(0)
            flag = 0
            for j in visit:
                if cmp[0] in j or cmp[1] in j:
                    visit.append(cmp)
                    if a in cmp:
                        cntA += len(visit)
                        visit = []
                    elif b in cmp:
                        cntB += len(visit)
                        visit = []
                    flag = 1
                    break
            if flag != 1:
                cpyWires.append(cmp)
            
        if minDiff > abs(cntA - cntB):
            minDiff = abs(cntA - cntB)
        wires.append(tmp)
    return minDiff

sol = solution(4, [[1,2],[2,3],[3,4]])
print(sol)
