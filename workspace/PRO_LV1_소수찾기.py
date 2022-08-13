def solution(n):
    answer = 0
    flag = 1
    
    for i in range(n):
        
        for j in range(i):
            target = i + 1
            tmp = j + 1
            
            if tmp != 1 and tmp != target:
                if target % tmp == 0:
                    flag = 1
                    break
                
        if flag == 1:
            flag = 0
            continue
        
        answer += 1
        
    return answer