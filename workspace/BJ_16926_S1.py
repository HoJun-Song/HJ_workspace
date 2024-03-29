from collections import deque

y, x, r = map(int, input().split())
A = []
for i in range(y):
    line = list(map(int, input().split()))
    A.append(line)

boundaryList = deque()
boundaryLength = min(x, y) // 2
for i in range(boundaryLength):
    boundary = deque()
    boundary.extend(A[i][i:x-i])
    boundary.extend(A[ty][x-i-1] for ty in range(i+1, y-i-1))
    boundary.extend(A[y-i-1][tx] for tx in range(x-i-1, i-1, -1))
    boundary.extend(A[ty][i] for ty in range(y-i-2, i, -1))
    boundaryList.append(boundary)

for boundary in boundaryList:
    for _ in range(r):
        tmp = boundary.popleft()
        boundary.append(tmp)

B = [[0] * x for _ in range(y)]
for i in range(boundaryLength):
    boundary = boundaryList.popleft()
    for j in range(i, x-i):
        B[i][j] = boundary.popleft()
    for j in range(i+1, y-i-1):
        B[j][x-i-1] = boundary.popleft()
    for j in range(x-i-1, i-1, -1):
        B[y-i-1][j] = boundary.popleft()
    for j in range(y-i-2, i, -1):
        B[j][i] = boundary.popleft()

for ty in range(y):
    for tx in range(x):
        print(B[ty][tx], end=' ')
    print('')




'''
크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.

A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
   ↓                                       ↑
A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
   ↓         ↓                   ↑         ↑
A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
   ↓                                       ↑
A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.

1 2 3 4       2 3 4 8       3 4 8 6
5 6 7 8       1 7 7 6       2 7 8 2
9 8 7 6   →   5 6 8 2   →   1 7 6 3
5 4 3 2       9 5 4 3       5 9 5 4
 <시작>         <회전1>        <회전2>
배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

입력
첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.

둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

출력
입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.

제한
2 ≤ N, M ≤ 300
1 ≤ R ≤ 1,000
min(N, M) mod 2 = 0
1 ≤ Aij ≤ 108
예제 입력 1
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
예제 출력 1
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
예제 입력 2
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
예제 출력 2
28 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1
예제 입력 3
2 2 3
1 1
1 1
예제 출력 3
1 1
1 1
'''