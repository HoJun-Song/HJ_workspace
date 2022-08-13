from itertools import combinations
def solution(nums):
    answer = 0

    test = list(combinations(nums, 3))
    
    for i in test:
        num = sum(i)
        flag = 0
        
        for j in range(num):
            if j == 0 or j == num - 1:
                continue
            if num % (j+1) == 0:
                flag = 1
                break;
                
        if flag == 0:
            answer += 1
            
    return answer
