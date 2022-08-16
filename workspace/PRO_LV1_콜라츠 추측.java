class Solution {
    public int solution(long num) {
        int answer = 0;
        while (answer <= 500) {
            if (num == 1) {
                break;
            }
            else {
                answer += 1;
                if ((num % 2) == 0) {
                    num /= 2;
                }
                else {
                    num *= 3;
                    num += 1;
                }
            }
        }

        if (answer > 500) {
            answer = -1;
        }
        return answer;
    }
}