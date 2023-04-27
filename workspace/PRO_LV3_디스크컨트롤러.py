def solution(jobs):
    answer = 0
    heap = []
    jobs.sort(key=lambda x: (x[0], x[1]))

    time = 0
    j = 0
    while j < len(jobs) or len(heap) > 0:
        while j < len(jobs):
            if jobs[j][0] <= time:
                heap.append(jobs[j])
                j += 1
            else:
                break

        if len(heap) > 0:
            heap.sort(key=lambda x: x[1], reverse=True)
            workJob = heap.pop()
            delayTime = time - workJob[0]
            answer += (delayTime + workJob[1])
            time += workJob[1]
        else:
            time += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[7, 8], [3, 5], [9, 6]]))