def solution(brown, yellow):
    total = brown + yellow
    for i in range(total // 2, 2, -1):
        if total % i == 0:
            x = total // i
            y = i
            if x < y:
                x, y = y, x
            cntB = 2 * (x + y - 2)
            if cntB == brown:
                answer = [x, y]
                return answer