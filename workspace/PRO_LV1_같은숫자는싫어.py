def solution(arr):
    answer = []
    for i in arr:
        if i in answer and i == answer[-1]:
            continue
        answer += [i]
    return answer