def solution(n, lost, reserve):
    arr = [1]
    arr = arr * n
    for i in lost:
        arr[i - 1] -= 1
    for i in reserve:
        arr[i - 1] += 1
        
    for i in range(len(arr)):
        if arr[i] == 0:
            if i == 0:
                if arr[i + 1] == 2:
                    arr[i] = 1
                    arr[i + 1] = 1
                    continue
                
            elif i == len(arr) - 1:
                if arr[i - 1] == 2:
                    arr[i] = 1
                    arr[i - 1] = 1
                    continue
            else:
                if arr[i - 1] == 2:
                    arr[i] = 1
                    arr[i - 1] = 1
                    continue
                
                if arr[i + 1] == 2:
                    arr[i] = 1
                    arr[i + 1] = 1
                    continue
            
            n -= 1
    
    return n