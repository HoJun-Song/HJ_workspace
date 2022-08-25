def Fibo(N):
    if N in fibo:
        return fibo[N]
    fibo[N] = [Fibo(N - 1)[0] + Fibo(N - 2)[0], Fibo(N - 1)[1] + Fibo(N - 2)[1]]
    return fibo[N]

T = int(input())
for _ in range(T):
    N = int(input())
    fibo = {}
    fibo[0] = [1, 0]
    fibo[1] = [0, 1]
    fibo[3] = [1, 2]
    fibo[6] = [5, 8]
    Fibo(N)
    n = fibo[N]
    print(n[0], n[1])