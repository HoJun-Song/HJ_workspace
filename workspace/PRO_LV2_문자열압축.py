def solution(s):
    answer = 0
    unit = 1
    answers = []
    
    while(unit <= len(s)):
        tmp = s[0:unit]
        result = ""
        count = 1
        i = unit

        while i <= (len(s) - 1):
            cmp = s[i:(i+unit)]
            if cmp == tmp:
                count += 1
            else:
                if count != 1:
                    result += str(count) + tmp
                else:
                    result += tmp
                count = 1
                tmp = cmp
                
            i += unit

        if count != 1:
            result += str(count) + tmp
        else:
            result += tmp
            result += s[i:]
        
        answers.append(len(result))
            
        unit += 1
        
    answer = min(answers)
    
    return answer