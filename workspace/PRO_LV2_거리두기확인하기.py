def solution(places):
    answer = []
    for room in places:
        posP = []
        posO = []
        flag = 0
        for i in range(len(room)):
            for j in range(len(room[i])):
                curSit = room[i][j]
                if curSit == 'P':
                    posP += [[i,j]]
                if curSit == 'O':
                    posO += [[i,j]]
        
        for i in range(len(posP)):
            curP = posP[i]
            if flag == 1:
                break;
            for j in range(len(posP) - i - 1):
                cmpP = (posP[j + i + 1])
                diffX = abs(curP[0] - cmpP[0])
                diffY = abs(curP[1] - cmpP[1])
                if (diffX + diffY <= 1):
                    answer.append(0)
                    flag = 1
                    break;
                elif (diffX + diffY == 2):
                    if (diffX == 2):
                        x = (curP[0] + cmpP[0]) / 2
                        [x1, y1] = [x, curP[1]]
                        if [x1, y1] in posO:
                            answer.append(0)
                            flag = 1
                            break;
                    elif (diffY == 2):
                        y = (curP[1] + cmpP[1]) / 2
                        [x1, y1] = [curP[0], y]
                        if [x1, y1] in posO:
                            answer.append(0)
                            flag = 1
                            break;
                    else:
                        [x1, y1] = [curP[0], cmpP[1]]
                        [x2, y2] = [cmpP[0], curP[1]]
                        if [x1, y1] in posO:
                            answer.append(0)
                            flag = 1
                            break;
                        elif [x2, y2] in posO:
                            answer.append(0)
                            flag = 1
                            break;
        if flag == 0:
            answer.append(1)
            flag = 0
    return answer
