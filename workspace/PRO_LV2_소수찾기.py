from itertools import permutations

def solution(numbers):
    answer = 0
    strNumbers = []
    for i in range(1, len(numbers) + 1):
        strNumbers.append(list(permutations(list(numbers), i)))

    intNumbers = set()
    for i in strNumbers:
        for strNum in i:
            tmp = "".join(strNum)
            intNumbers.add(int(tmp))

    for num in intNumbers:
        if sosu(num): answer += 1

    return answer

def sosu(num):
    if num > 2 and num % 2 == 0: return False
    elif num < 2: return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

print(solution("011"))