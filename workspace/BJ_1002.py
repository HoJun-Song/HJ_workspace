X = int(input())

for _ in range(X):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    diff12 = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    sumR = r1 + r2
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if diff12 > sumR:
            print(0)
        elif diff12 == sumR:
            print(1)
        else:
            smallR = min(r1, r2)
            bigR = max(r1, r2)
            if diff12 + smallR == bigR:
                print(1)
            elif diff12 + smallR < bigR:
                print(0)
            else:
                print(2)