class Solution {
    public int[] solution(int n, int m) {
        if (n > m) {
            int tmp = n;
            n = m;
            m = tmp;
        }

        int gcd = 0;
        int lcm = n * m;
        while (true) {
            gcd = m % n;
            if (gcd == 0) {
                gcd = n;
                break;
            }
            else {
                m = n;
                n = gcd;
            }
        }
        lcm /= gcd;

        int[] answer = {gcd, lcm};
        return answer;
    }
}