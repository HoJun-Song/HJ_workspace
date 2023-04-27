import functools

def solution(numbers):
    arr = list(map(str, numbers))
    arr = sorted(arr, key=functools.cmp_to_key(comp))
    if "".join(arr)[0] == '0':
        return str(0)
    else:
        return "".join(arr)

def comp(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)

    if int(xy) < int(yx):
        return 1
    else:
        return -1

sol = solution([0,0,2,21,1])
print(sol)