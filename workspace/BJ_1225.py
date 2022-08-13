A, B = map(int, input().split())
i = 10
num_A = []
num_B = []
while A // i > 0:
    tmp = A % i
    num_A.append(tmp)
    A = A // i
num_A.append(A % i)
while B // i > 0:
    tmp = B % i
    num_B.append(tmp)
    B = B // i
num_B.append(B % i)
mul = sum(num_A) * sum(num_B)
print(mul)
