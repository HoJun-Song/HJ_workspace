def solution(w,h):
    totalCount = w * h
    
    if w == h:
        return totalCount - w
    
    i = min(w, h)
    while True:
        if w%i == 0 and h%i ==0:
            break
        else:
            i -= 1
    
    answer = totalCount - (w + h - i)
    return answer