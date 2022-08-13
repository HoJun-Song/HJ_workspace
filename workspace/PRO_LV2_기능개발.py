import math
def solution(progresses, speeds):
    answer = []
    modProgress = []
    for i in progresses:
        modProgress.append(100 - i)
        
    modDay = []
    for i in range(len(speeds)):
        modDay.append(math.ceil(modProgress[i] / speeds[i]))
    
    work = modDay.pop(0)
    count = 1
    
    while len(modDay) > 0:
        tmp = modDay.pop(0)
        
        if tmp > work:
            work = tmp
            answer.append(count)
            count = 1
        else:
            count += 1
            
            
    answer.append(count)
    return answer