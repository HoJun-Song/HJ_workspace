def solution(s):
    stack = list(s)
    cnt1 = 0
    while len(stack) > 0:
        chr = stack.pop()
        if chr == '(':
            if cnt1 == 0:
                return False
            else:
                cnt1 -= 1
                continue
        cnt1 += 1
    
    if cnt1 != 0:
        return False
        
    return True