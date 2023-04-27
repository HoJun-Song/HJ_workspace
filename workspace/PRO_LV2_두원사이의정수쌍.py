import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        answer += countY(x, r1, r2)

    return answer * 4

def countY(x, r1, r2):
    maxY = math.floor((r2**2 - x**2)**(1/2))
    if r1**2 - x**2 <= 0:
        minY = 0
    else:
        minY = math.ceil((r1**2 - x**2)**(1/2))
    return maxY - minY + 1

print(solution(2, 3))