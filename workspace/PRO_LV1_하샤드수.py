def solution(x):
    answer = False
    originX = x
    tmp = 0
    while (x > 0):
        tmp += (x % 10)
        x //= 10
    if (originX % tmp) == 0:
        answer = True
    return answer