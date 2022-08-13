#include <stdio.h>
#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string>

using namespace std;

#define TERMINAL_NUM 4
#define CHIP_LENGTH 8

int main()
{
    pid_t send_p[TERMINAL_NUM]; //4개의 전송 프로세스
    pid_t receive_p[TERMINAL_NUM]; //4개의 수신 프로세스

    int bit_data[TERMINAL_NUM]; //각 프로세스의 비트 데이터
    int chip_data[TERMINAL_NUM][CHIP_LENGTH]; //각 프로세스의 칩 시퀀스
    int send_data[TERMINAL_NUM][CHIP_LENGTH]; //각 전송 프로세스의 계산된 전송할 신호
    int combine_data[CHIP_LENGTH] = {0}; //joiner프로세스의 결합된 신호
    int receive_data[CHIP_LENGTH] = {0}; //각 수신 프로세스의 계산된 수신된 신호

    int pipes[2]; //프로세스간 통신용 파이프 (write, read 2개)
    int buffer[CHIP_LENGTH]; //파이프에서 읽어올 데이터 버퍼

    pipe(pipes); //파이프 생성

    cout << "비트 4개를 입력하세요." << endl; //전송할 4개의 비트 입력
    for (int i = 0; i < TERMINAL_NUM; i++) { //각 프로세스에 전송할 비트 할당
        cout << "t" << i << "의 비트: ";
        cin >> bit_data[i];

        if (bit_data[i] == 0) { //bipolar notation이므로 1, -1 중 하나의 값을 가진다.
            bit_data[i] = -1; //따라서 0일 경우를 -1로 변환
        }
    }

    cout << endl << "길이가 8인 칩 시퀀스 4개를 입력하세요." << endl; //전송할 4개의 칩 시퀀스 입력
    for (int i = 0; i < TERMINAL_NUM; i++) {
        cout << "t" << i << "의 칩 시퀀스: ";
        for (int j = 0; j < CHIP_LENGTH; j++) { //각 프로세스에 칩 시퀀스 할당
            cin >> chip_data[i][j];

            if (chip_data[i][j] == 0) { //bipolar notation이므로 1, -1 중 하나의 값을 가진다.
                chip_data[i][j] = -1; //따라서 0일 경우를 -1로 변환
            }
        }
    }

    //전송 프로세스 생성 후 각 신호를 계산하여 joiner프로세스에 전달하고
    //joiner프로세스는 이 신호들을 결합하여 저장
    for (int i = 0; i < TERMINAL_NUM; i++) {
        send_p[i] = fork(); //전송 프로세스 생성
        if (send_p[i] < 0) { //프로세스 생성 에러
            cout << "프로세스 생성 에러" << endl;
            return -1;
        }
        else if (send_p[i] == 0) { //자식 프로세스 생성
            for (int j = 0; j < CHIP_LENGTH; j++) { //전송할 각 신호 계산
                send_data[i][j] = bit_data[i] * chip_data[i][j];
            }

            write(pipes[1], send_data[i], 32); //계산된 신호를 파이프에 쓰기
            exit(1);
        }
        else {
            read(pipes[0], buffer, 32); //파이프에 있는 신호 읽기
            for (int i = 0; i < CHIP_LENGTH; i++) {
                combine_data[i] += buffer[i]; //전달받은 신호들을 결합
            }
            wait(NULL);
        }
    }

    //결합된 신호 출력
    cout << endl << "결합된 신호" << endl;
    for (int i = 0; i < CHIP_LENGTH; i++) {
        cout << combine_data[i] << " ";
    }
    cout << endl << endl;

    //수신 프로세스 생성 후 joiner프로세스에서 전달받은 결합된 신호를
    //계산하여 표준 출력으로 화면에 출력
    for (int i = 0; i < TERMINAL_NUM; i++) {
        receive_p[i] = fork(); //수신 프로세스 생성
        if (receive_p[i] < 0) { //프로세스 생성 에러
            cout << "프로세스 생성 에러" << endl;
            return -1;
        }
        else if (receive_p[i] == 0) { //자식 프로세스 생성
            read(pipes[0], buffer, 32); //파이프에 있는 신호 읽기
            for (int j = 0; j < CHIP_LENGTH; j++) {
                receive_data[i] += chip_data[i][j] * buffer[j]; //전달 받은 신호 계산
            }

            //계산된 각 프로세스의 신호를 표준 출력으로 화면에 출력
            if (receive_data[i] / CHIP_LENGTH == 1)
                cout << "r" << i << "에서 수신된 비트: 1" << endl;
            else if (receive_data[i] / CHIP_LENGTH == -1)
                cout << "r" << i << "에서 수신된 비트: 0" << endl;

            exit(1);
        }
        else {
            write(pipes[1], combine_data, 32); //joiner프로세스에서 결합된 신호를 파이프에 쓰기
            wait(NULL);
        }
    }
}
