def solution(phone_number):
    phoneLength = len(phone_number)
    answer = list(phone_number)
    for i in range(phoneLength - 4):
        answer[i] = '*'
    answer = "".join(answer)
    return answer