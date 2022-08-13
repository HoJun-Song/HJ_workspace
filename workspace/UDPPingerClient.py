'''
2017112096 송호준
UDPPingerClient.py
'''
import time
from socket import *

# Server의 IP
serverIP = '127.0.0.1'
# Server의 Port Number
serverPort = 12000

# Create a UDP socket 
# Create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# timeout 1초로 설정
clientSocket.settimeout(1)

print("=======Client is running=======")

# packet loss 카운팅
lossCnt = 0
# 모든 통신의 RTT값을 배열로 저장
RTT = []

# sequenceNum을 1부터 10까지 1씩 증가시키며 총 10번 반복
for sequenceNum in range(1, 11):
    # message에 ping + sequence number 저장
    message = "Ping " + str(sequenceNum)
    # client socket에서 message를 인코딩하여 server socket으로 전송
    clientSocket.sendto(message.encode("utf-8"), (serverIP, serverPort))
    # client에서 보낸 시간
    sendTime = time.time()

    try:
        # server로부터 message를 수신
        message, address = clientSocket.recvfrom(1024)
        # 수신 시간 - 보낸 시간으로 RTT 계산
        rtt = time.time()-sendTime
        # RTT배열에 현재 rtt추가
        RTT.append(rtt)
        # server로부터 받은 message를 디코딩하여 rtt와 함께 출력
        print(str(message.decode()) + "    RTT: %f" %rtt + "sec")
        
    # timeout이 발생하면 except처리
    except timeout:
        #lossCnt를 1증가시키고 실패 message 출력
        lossCnt += 1
        print(message + "    Request timed out")

# close socket
clientSocket.close()

#Optional Exercises
print("===============================")
# 최소, 최대, 평균 RTT를 계산하여 출력
print("Minimum RTT: %fsec" %min(RTT) + "\nMaximum RTT: %fsec" %max(RTT) + "\nAverage RTT: %fsec" %(sum(RTT)/len(RTT)))
print("===============================")
# packet loss rate를 계산하여 출력
print("Packet loss rate: " + str(lossCnt * 10) + "%")
