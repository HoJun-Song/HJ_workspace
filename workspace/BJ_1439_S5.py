S = input()
cnt = 0
i = 1
curChar = S[0]
while i < len(S):
    nextChar = S[i]
    if nextChar != curChar:
        cnt += 1
        curChar = nextChar
    i += 1

if cnt % 2 == 0:
    print(cnt // 2)
else:
    print((cnt // 2) + 1)
