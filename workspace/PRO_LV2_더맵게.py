import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            minScoville = heapq.heappop(scoville)
            tmpScoville = heapq.heappop(scoville)
            sumScoville = minScoville + (tmpScoville * 2)
            heapq.heappush(scoville, sumScoville)
            answer += 1
    return answer