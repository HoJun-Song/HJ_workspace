def solution(clothes):
    clothesType = []
    for i in clothes:
        tmp = i[1]
        flag = 0
        for j in range(len(clothesType)):
            if tmp == clothesType[j][0]:
                flag = 1
                clothesType[j][1] += 1
                break
            
        if flag == 0:
            clothesType.append([i[1], 1])
    
    answer = 1
    for i in clothesType:
        answer *= (i[1] + 1)
    answer -= 1
        
    return answer