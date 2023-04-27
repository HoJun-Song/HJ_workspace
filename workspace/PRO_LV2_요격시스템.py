def solution(targets):
    answer = 1

    i = 0
    targets.sort(key=lambda x: x[1])
    endX = targets[0][1]
    while i < len(targets):
        if endX <= targets[i][0]:
            endX = targets[i][1]
            answer += 1
        i += 1

    return answer


print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))