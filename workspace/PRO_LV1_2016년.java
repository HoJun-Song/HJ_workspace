class Solution {
    public String solution(int a, int b) {
        String[] answer = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int date = 4;
        for (int i = 1; i < a; i++) {
            if (i <= 7) {
                if (i % 2 == 1) {
                    date += 31;
                }
                else if (i == 2) {
                    date += 29;
                }
                else {
                    date += 30;
                }
            }
            else {
                if (i % 2 == 0) {
                    date += 31;
                }
                else {
                    date += 30;
                }
            }

        }
        
        date += b;
        
        return answer[date % 7];
    }
}
