def solution(priorities, location):
    answer = 0
    pri = max(priorities)
    i = location
    while (True):
        if priorities[0] != pri:
            if i != 0:
                i -= 1
            else:
                i = len(priorities) - 1
            tmp = priorities.pop(0)
            priorities.append(tmp)
        else:
            priorities.pop(0)
            answer += 1
            if i == 0:
                return answer
            i -= 1
            pri = max(priorities)