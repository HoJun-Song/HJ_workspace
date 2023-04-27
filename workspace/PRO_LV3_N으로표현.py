def solution(N, number):
    if N == number: return 1

    result = {1: {N}}
    for i in range(2, 9):
        tmpResult = set()
        tmpResult.update(calculate(i, result))
        tmpResult.add(int(str(N) * i))
        if number in tmpResult:
            return i
        else:
            result[i] = tmpResult

    return -1

def calculate(i, result):
    tmpSet = set()
    for x in range(1, i):
        ls = list(map(int, result[x]))
        rs = list(map(int, result[i - x]))
        for l in ls:
            for r in rs:
                tmpSet.add(l+r)
                tmpSet.add(l*r)
                if r != 0: tmpSet.add(l//r)
                tmpSet.add(l-r)

    return tmpSet

print(solution(5, 12))
print(solution(2, 11))