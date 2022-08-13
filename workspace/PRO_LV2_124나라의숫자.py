def solution(n):
    answer = ''
    arr = []
    n = int(n)
    
    while n >= 1:
        tmp = n % 3
        if tmp == 0:
            tmp = 4
            n -= 1
        arr.append(tmp)
        n = n // 3
        
    arr.reverse()
    
    for i in arr:
        answer += str(i)
    
    return answer