def solution(prices):
    answer = []
    for i in range(len(prices)):
        tmp = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                tmp += 1
            else:
                tmp += 1
                break
        answer += [tmp]

    return answer

"""
결론! slice[:]는 오래걸린다!
스택쓰는 방법 있는데..뭔소린지..
"""