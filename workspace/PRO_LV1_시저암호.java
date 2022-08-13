class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for (int i = 0; i < s.length(); i++) {
            char num = s.charAt(i);
            int ascii = num + n;
            
            if (num == ' ') {
                answer += ' ';
                continue;
            }
            else if (num >= 65 && num <= 90) {
                if (ascii > 90) ascii -= 26;
            }
            else if (num >= 97) {
                if (ascii > 122) ascii -= 26;
            }

            answer += (char)ascii;
        }
        return answer;
    }
}