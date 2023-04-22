N = int(input())

cmdList = [input() for _ in range (N)]

result = ""
for i in range (len(cmdList[0])):
    tmp = cmdList[0][i]
    for j in range (1, N):
        if (cmdList[j][i] != tmp): tmp = '?'
    result += tmp
print(result)