//2022-07-25 시간초과
class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            int mod = 0;
            int j = 2;
            while (j <= i) {
                if (i%j == 0) mod += 1;
                if (mod > 1) break;
                j += 1;
            }
            if (mod == 1) answer += 1;
        }
        return answer;
    }
}