import collections
import itertools

def solution(genres, plays):
    answer = []
    genresDict = {}
    genresPlayDict = {}
    for i in range(len(genres)):
        if genres[i] in genresDict:
            genresDict[genres[i]] += [[plays[i], i]]
            genresPlayDict[genres[i]] = [genres[i], genresPlayDict[genres[i]][1] + plays[i]]
        else:
            genresDict[genres[i]] = [[plays[i], i]]
            genresPlayDict[genres[i]] = [genres[i], plays[i]]

    genresPlayMap = list(genresPlayDict.values())
    genresPlayMap.sort(key=lambda x: x[1], reverse=True)

    for genre in genresPlayMap:
        genreList = list(genresDict[genre[0]])
        genreList.sort(key=lambda x: (x[0], -x[1]))
        if len(genreList) > 0:
            answer.append(genreList.pop()[1])
        if len(genreList) > 0:
            answer.append(genreList.pop()[1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))