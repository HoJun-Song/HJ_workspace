from itertools import combinations
def solution(numbers, target):
    answer = 0
    numbers.sort()
    maxN = sum(numbers)
    if target > maxN:
        return 0
    elif target == maxN:
        return 1
    else:
        for i in range(1, len(numbers)):
            sumN = 0
            combList = list(combinations(numbers, i))
            for j in combList:
                sumN = sum(j)
                if maxN - 2 * sumN == target:
                    answer += 1
    return answer