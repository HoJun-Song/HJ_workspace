def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        cnt, charI = 0, 0
        cmp, partStr, string = "", "", ""

        while charI < len(s):
            if len(string) >= answer: break

            partStr = s[charI: charI + i]
            charI += i

            if cmp == "" or cmp == partStr:
                cmp = partStr
                cnt += 1
            else:
                if cnt <= 1:
                    string += cmp
                else:
                    string += (str(cnt) + cmp)
                cmp = partStr
                cnt = 1

        if len(string) >= answer:
            continue

        if cnt <= 1:
            string += cmp
        else:
            string += (str(cnt) + cmp)

        if answer > len(string):
            answer = len(string)

    return answer

print(solution("ababcdcdababcdcd"))