def solution(genres, plays):
    answer = []
    arr1 = []
    for i in range(len(genres)):
        tmp = genres[i]
        flag = 0
        for j in range(len(arr1)):
            if tmp == arr1[j][0]:
                flag = 1
                arr1[j][1] += plays[i]
                break
        if flag == 0:
            arr1.append([genres[i], plays[i]])
    
    arr1.sort(key=lambda x: x[1])
    
    while (len(arr1) > 0):
        maxMusic = arr1.pop()
        musicList = []
        for i in range(len(genres)):
            if maxMusic[0] == genres[i]:
                musicList.append([i, plays[i]])
        musicList.sort(key=lambda x: x[1], reverse=1)
        
        count = 0
        for i in musicList:
            answer.append(i[0])
            count += 1
            if count == 2:
                break
    
    return answer