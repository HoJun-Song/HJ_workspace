g, lenS = map(int, input().split())
W = input()
S = input()

# A65 - z122
wa = [0] * 58
sa = [0] * 58

for i in W:
    wa[ord(i) - 65] += 1

start, length = 0, 0
cnt = 0
while start < lenS:
    sa[ord(S[start]) - 65] += 1
    length += 1

    if length == g:
        if wa == sa:
            cnt += 1
        sa[ord(S[start - g + 1]) - 65] -= 1
        length -= 1

    start += 1

print(cnt)

"""
슬라이딩 윈도우
"""