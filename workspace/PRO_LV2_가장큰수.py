#2022-07-11 2차 시도
def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=lambda x: (x[0:1],
                            x[0:1] if len(x) == 1 else x[1:2],
                            x[1:2] if len(x) == 2 else x[2:3],
                            x[2:3] if len(x) == 3 else x[3:4]), reverse=True)
    answer = "".join(arr)
    tmp = int(answer)
    answer = str(tmp)
    return answer

sol = solution([9, 998])
print(sol)