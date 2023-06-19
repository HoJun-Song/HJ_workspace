y, x, R = map(int, input().split())
A = []
for i in range(y):
    line = input().split()
    A.append(line)
cmdList = list(map(int, input().split()))

for cmd in cmdList:
    if cmd == 1:
        # 상하 반전
        tmp = []
        for i in range(y):
            tmp.append(A[y - i - 1])
        A = tmp

    elif cmd == 2:
        # 좌우 반전
        tmp = []
        for i in range(y):
            tmp.append(list(reversed(A[i])))
        A = tmp

    elif cmd == 3:
        # 시계방향 회전 90도
        tmp = []
        for i in range(x):
            line = []
            for j in range(y):
                line.append(A[y - j - 1][i])
            tmp.append(line)
        A = tmp
        x, y = y, x

    elif cmd == 4:
        # 반시계방향 회전 90도
        tmp = []
        for i in range(x):
            line = []
            for j in range(y):
                line.append(A[j][x - i - 1])
            tmp.append(line)
        A = tmp
        x, y = y, x

    elif cmd == 5:
        # 4블록 나눠서 블록끼리 시계방향 회전
        tmp = []
        for i in range(y // 2):
            line = []
            for j in range(x // 2):
                line.append(A[i + y // 2][j])
            for j in range(x // 2):
                line.append(A[i][j])
            tmp.append(line)

        for i in range(y // 2):
            line = []
            for j in range(x // 2):
                line.append(A[i + y // 2][j + x // 2])
            for j in range(x // 2):
                line.append(A[i][j + x // 2])
            tmp.append(line)
        A = tmp

    elif cmd == 6:
        # 4블록 나눠서 블록끼리 반시계방향 회전
        tmp = []
        for i in range(y // 2):
            line = []
            for j in range(x // 2):
                line.append(A[i][j + x // 2])
            for j in range(x // 2):
                line.append(A[i + y // 2][j + x // 2])
            tmp.append(line)

        for i in range(y // 2):
            line = []
            for j in range(x // 2):
                line.append(A[i][j])
            for j in range(x // 2):
                line.append(A[i + y // 2][j])
            tmp.append(line)
        A = tmp

for i in range(y):
    for j in range(x):
        print(A[i][j] + ' ', end='')
    print()

'''
크기가 N×M인 배열이 있을 때, 배열에 연산을 R번 적용하려고 한다. 연산은 총 6가지가 있다.

1번 연산은 배열을 상하 반전시키는 연산이다.

1 6 2 9 8 4 → 4 2 9 3 1 8
7 2 6 9 8 2 → 9 2 3 6 1 5
1 8 3 4 2 9 → 7 4 6 2 3 1
7 4 6 2 3 1 → 1 8 3 4 2 9
9 2 3 6 1 5 → 7 2 6 9 8 2
4 2 9 3 1 8 → 1 6 2 9 8 4
   <배열>       <연산 결과>
2번 연산은 배열을 좌우 반전시키는 연산이다.

1 6 2 9 8 4 → 4 8 9 2 6 1
7 2 6 9 8 2 → 2 8 9 6 2 7
1 8 3 4 2 9 → 9 2 4 3 8 1
7 4 6 2 3 1 → 1 3 2 6 4 7
9 2 3 6 1 5 → 5 1 6 3 2 9
4 2 9 3 1 8 → 8 1 3 9 2 4
   <배열>       <연산 결과>
3번 연산은 오른쪽으로 90도 회전시키는 연산이다.

1 6 2 9 8 4 → 4 9 7 1 7 1
7 2 6 9 8 2 → 2 2 4 8 2 6
1 8 3 4 2 9 → 9 3 6 3 6 2
7 4 6 2 3 1 → 3 6 2 4 9 9
9 2 3 6 1 5 → 1 1 3 2 8 8
4 2 9 3 1 8 → 8 5 1 9 2 4
   <배열>       <연산 결과>
4번 연산은 왼쪽으로 90도 회전시키는 연산이다.

1 6 2 9 8 4 → 4 2 9 1 5 8
7 2 6 9 8 2 → 8 8 2 3 1 1
1 8 3 4 2 9 → 9 9 4 2 6 3
7 4 6 2 3 1 → 2 6 3 6 3 9
9 2 3 6 1 5 → 6 2 8 4 2 2
4 2 9 3 1 8 → 1 7 1 7 9 4
   <배열>       <연산 결과>
5, 6번 연산을 수행하려면 배열을 크기가 N/2×M/2인 4개의 부분 배열로 나눠야 한다. 아래 그림은 크기가 6×8인 배열을 4개의 그룹으로 나눈 것이고, 1부터 4까지의 수로 나타냈다.

1 1 1 1 2 2 2 2
1 1 1 1 2 2 2 2
1 1 1 1 2 2 2 2
4 4 4 4 3 3 3 3
4 4 4 4 3 3 3 3
4 4 4 4 3 3 3 3
5번 연산은 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산이다.

3 2 6 3 1 2 9 7 → 2 1 3 8 3 2 6 3
9 7 8 2 1 4 5 3 → 1 3 2 8 9 7 8 2
5 9 2 1 9 6 1 8 → 4 5 1 9 5 9 2 1
2 1 3 8 6 3 9 2 → 6 3 9 2 1 2 9 7
1 3 2 8 7 9 2 1 → 7 9 2 1 1 4 5 3
4 5 1 9 8 2 1 3 → 8 2 1 3 9 6 1 8
     <배열>            <연산 결과>
6번 연산은 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산이다.

3 2 6 3 1 2 9 7 → 1 2 9 7 6 3 9 2
9 7 8 2 1 4 5 3 → 1 4 5 3 7 9 2 1
5 9 2 1 9 6 1 8 → 9 6 1 8 8 2 1 3
2 1 3 8 6 3 9 2 → 3 2 6 3 2 1 3 8
1 3 2 8 7 9 2 1 → 9 7 8 2 1 3 2 8
4 5 1 9 8 2 1 3 → 5 9 2 1 4 5 1 9
     <배열>            <연산 결과>
입력
첫째 줄에 배열의 크기 N, M과 수행해야 하는 연산의 수 R이 주어진다.

둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

마지막 줄에는 수행해야 하는 연산이 주어진다. 연산은 공백으로 구분되어져 있고, 문제에서 설명한 연산 번호이며, 순서대로 적용시켜야 한다.

출력
입력으로 주어진 배열에 R개의 연산을 순서대로 수행한 결과를 출력한다.

제한
2 ≤ N, M ≤ 100
1 ≤ R ≤ 1,000
N, M은 짝수
1 ≤ Aij ≤ 108
예제 입력 1
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
1
예제 출력 1
4 5 1 9 8 2 1 3
1 3 2 8 7 9 2 1
2 1 3 8 6 3 9 2
5 9 2 1 9 6 1 8
9 7 8 2 1 4 5 3
3 2 6 3 1 2 9 7
예제 입력 2
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
2
예제 출력 2
7 9 2 1 3 6 2 3
3 5 4 1 2 8 7 9
8 1 6 9 1 2 9 5
2 9 3 6 8 3 1 2
1 2 9 7 8 2 3 1
3 1 2 8 9 1 5 4
예제 입력 3
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
3
예제 출력 3
4 1 2 5 9 3
5 3 1 9 7 2
1 2 3 2 8 6
9 8 8 1 2 3
8 7 6 9 1 1
2 9 3 6 4 2
1 2 9 1 5 9
3 1 2 8 3 7
예제 입력 4
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
4
예제 출력 4
7 3 8 2 1 3
9 5 1 9 2 1
2 4 6 3 9 2
1 1 9 6 7 8
3 2 1 8 8 9
6 8 2 3 2 1
2 7 9 1 3 5
3 9 5 2 1 4
예제 입력 5
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
5
예제 출력 5
2 1 3 8 3 2 6 3
1 3 2 8 9 7 8 2
4 5 1 9 5 9 2 1
6 3 9 2 1 2 9 7
7 9 2 1 1 4 5 3
8 2 1 3 9 6 1 8
예제 입력 6
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
6
예제 출력 6
1 2 9 7 6 3 9 2
1 4 5 3 7 9 2 1
9 6 1 8 8 2 1 3
3 2 6 3 2 1 3 8
9 7 8 2 1 3 2 8
5 9 2 1 4 5 1 9
예제 입력 7
6 8 6
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
1 2 3 4 5 6
예제 출력 7
3 1 2 8 9 1 5 4
1 2 9 7 8 2 3 1
2 9 3 6 8 3 1 2
8 1 6 9 1 2 9 5
3 5 4 1 2 8 7 9
7 9 2 1 3 6 2 3
'''