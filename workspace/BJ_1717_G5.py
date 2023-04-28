n, m = map(int, input().split())

setList = {}

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        if a in setList:
            setList[a] += [b]
        else:
            setList[a] = [b]
        if b in setList:
            setList[b] += [a]
        else:
            setList[b] = [a]
    else:
        true = "NO"
        for set in setList.values():
            if a in set and b in set:
                true = "YES"
                break
        print(true)
