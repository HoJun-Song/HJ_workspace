def solution(sequence, k):
    answer = []

    if k in sequence:
        return [sequence.index(k), sequence.index(k)]

    l = 0
    r = 1
    tmpSum = sequence[l]
    length = len(sequence)
    while l < length - 1:
        if tmpSum == k:
            if len(answer) < 1:
                answer = [l, r - 1]
            else:
                diff = answer[1] - answer[0]
                if diff > r - 1 - l:
                    answer = [l, r - 1]
            if r < length:
                tmpSum += sequence[r]
                r += 1
            tmpSum -= sequence[l]
            l += 1
            continue
        elif tmpSum > k:
            tmpSum -= sequence[l]
            l += 1
        else:
            if r < length:
                tmpSum += sequence[r]
                r += 1
            else:
                tmpSum -= sequence[l]
                l += 1

    return answer