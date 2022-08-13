T = int(input())
while T:
    T -= 1
    a, b = map(int, (input().split()))
    one = a % 10
    if one == 0 or one == 1 or one == 5 or one == 6:
        if one == 0:
            one = 10
        print(one)
    elif one == 2:
        list = [2, 4, 8, 6]
        print(list[b % 4 - 1])
    elif one == 3:
        list = [3, 9, 7, 1]
        print(list[b % 4 - 1])
    elif one == 4:
        list = [4, 6]
        print(list[b % 2 - 1])
    elif one == 7:
        list = [7, 9, 3, 1]
        print(list[b % 4 - 1])
    elif one == 8:
        list = [8, 4, 2, 6]
        print(list[b % 4 - 1])
    elif one == 9:
        list = [9, 1]
        print(list[b % 2 - 1])
