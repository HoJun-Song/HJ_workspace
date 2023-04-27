import heapq

def solution(operations):
    minHeap = []
    maxHeap = []
    insertCnt = 0
    for operation in operations:
        key, value = operation.split()
        if key == 'I':
            insertCnt += 1
            heapq.heappush(minHeap, int(value))
            heapq.heappush(maxHeap, -int(value))
        elif value == '1' and len(maxHeap) > 0:
            insertCnt -= 1
            heapq.heappop(maxHeap)
        elif len(minHeap) > 0:
            insertCnt -= 1
            heapq.heappop(minHeap)

    for i in range(len(maxHeap)):
        maxHeap[i] = -maxHeap[i]

    heap = list(set(minHeap) & set(maxHeap))
    heap.sort()

    if insertCnt > 0:
        return [heap[-1], heap[0]]
    return [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))