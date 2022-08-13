X = int(input())
count = 1
stick = [64]
while True:
    if X < sum(stick):
        stick.sort()
        tmp = stick.pop(0) // 2
        stick.append(tmp)
        stick.append(tmp)
        count += 1
        stick.sort()
        if X <= (sum(stick) - stick[0]):
            stick.pop(0)
            count -= 1
    elif X >= sum(stick):
        break
print(count)
