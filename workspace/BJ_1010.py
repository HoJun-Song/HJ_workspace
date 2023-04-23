T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    num = x - 1
    mul = y
    div = x
    for i in range(num):
        y -= 1
        x -= 1
        mul *= y
        div *= x
    print(int(mul / div))