def solution(numbers, hand):
    answer = ''
    leftPos = [0, 3]
    rightPos = [2, 3]
    diffLeft = 0
    diffRight = 0
    
    for i in numbers:
        if i == 1:
            answer += 'L'
            leftPos = [0, 0]
        elif i == 4:
            answer += 'L'
            leftPos = [0, 1]
        elif i == 7:
            answer += 'L'
            leftPos = [0, 2]
        elif i == 3:
            answer += 'R'
            rightPos = [2, 0]
        elif i == 6:
            answer += 'R'
            rightPos = [2, 1]
        elif i == 9:
            answer += 'R'
            rightPos = [2, 2]
        elif i == 2:
            diffLeft = abs(leftPos[0] - 1) + abs(leftPos[1])
            diffRight = abs(rightPos[0] - 1) + abs(rightPos[1])
            if diffLeft < diffRight:
                answer += 'L'
                leftPos = [1, 0]
            elif diffLeft > diffRight:
                answer += 'R'
                rightPos = [1, 0]
            else:
                if hand == 'right':
                    answer += 'R'
                    rightPos = [1, 0]
                else:
                    answer += 'L'
                    leftPos = [1, 0]
        elif i == 5:
            diffLeft = abs(leftPos[0] - 1) + abs(leftPos[1] - 1)
            diffRight = abs(rightPos[0] - 1) + abs(rightPos[1] - 1)
            if diffLeft < diffRight:
                answer += 'L'
                leftPos = [1, 1]
            elif diffLeft > diffRight:
                answer += 'R'
                rightPos = [1, 1]
            else:
                if hand == 'right':
                    answer += 'R'
                    rightPos = [1, 1]
                else:
                    answer += 'L'
                    leftPos = [1, 1]
        elif i == 8:
            diffLeft = abs(leftPos[0] - 1) + abs(leftPos[1] - 2)
            diffRight = abs(rightPos[0] - 1) + abs(rightPos[1] - 2)
            if diffLeft < diffRight:
                answer += 'L'
                leftPos = [1, 2]
            elif diffLeft > diffRight:
                answer += 'R'
                rightPos = [1, 2]
            else:
                if hand == 'right':
                    answer += 'R'
                    rightPos = [1, 2]
                else:
                    answer += 'L'
                    leftPos = [1, 2]
        elif i == 0:
            diffLeft = abs(leftPos[0] - 1) + abs(leftPos[1] - 3)
            diffRight = abs(rightPos[0] - 1) + abs(rightPos[1] - 3)
            if diffLeft < diffRight:
                answer += 'L'
                leftPos = [1, 3]
            elif diffLeft > diffRight:
                answer += 'R'
                rightPos = [1, 3]
            else:
                if hand == 'right':
                    answer += 'R'
                    rightPos = [1, 3]
                else:
                    answer += 'L'
                    leftPos = [1, 3]
    return answer
