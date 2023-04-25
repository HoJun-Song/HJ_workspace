def solution(clothes):
    dictClothes = {}
    for clotheName, clotheType in clothes:
        if clotheType in dictClothes:
            dictClothes[clotheType] = dictClothes.get(clotheType) + [clotheName]
        else:
            dictClothes[clotheType] = [clotheName]

    answer = 1
    for clothesCount in dictClothes.values():
        answer *= (len(clothesCount) + 1)

    return answer - 1