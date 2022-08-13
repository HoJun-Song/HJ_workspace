def solution(record):
    answer = []
    dictonary = {}
    
    for sentence in record:
        act = sentence.split(" ")
        if len(act) > 2:
            dictonary[act[1]] = act[2]
            
    for sentence in record:
        act = sentence.split(" ")
        if act[0] == "Enter":
            user = dictonary.get(act[1])
            answer.append(user + "님이 들어왔습니다.")
        elif act[0] == "Leave":
            user = dictonary.get(act[1])
            answer.append(user + "님이 나갔습니다.")
    
    return answer
