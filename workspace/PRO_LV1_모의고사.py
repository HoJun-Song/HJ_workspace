def solution(answers):
    point = [0, 0, 0]
    
    for i in range(len(answers)):
        tmpA = (i % 5) + 1
        if tmpA == answers[i]:
            point[0] += 1
            
        if (i + 1) % 2 == 1:
            if answers[i] == 2:
                point[1] += 1
        else:
            tmp = (i + 1) % 8
            if tmp // 2 == 1 and answers[i] == 1:
                point[1] += 1
            elif tmp // 2 == 2 and answers[i] == 3:
                point[1] += 1
            elif tmp // 2 == 3 and answers[i] == 4:
                point[1] += 1
            elif tmp // 2 == 0 and answers[i] == 5:
                point[1] += 1
                
        tmpC = i % 10
        if tmpC // 2 <= 0:
            if answers[i] == 3:
                point[2] += 1
        elif tmpC // 2 <= 1:
            if answers[i] == 1:
                point[2] += 1
        elif tmpC // 2 <= 2:
            if answers[i] == 2:
                point[2] += 1
        elif tmpC // 2 <= 3:
            if answers[i] == 4:
                point[2] += 1
        elif tmpC // 2 <= 4:
            if answers[i] == 5:
                point[2] += 1
    
    print(point)
    tmpMax = max(point)
    answer = []
    for i in range(len(point)):
        if point[i] == tmpMax:
            answer.append(i + 1)
    
    return answer