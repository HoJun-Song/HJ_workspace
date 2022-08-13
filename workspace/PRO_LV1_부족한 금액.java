class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        
        long total = ((long)count * ((long)price + ((long)price * (long)count))) / 2;
        answer = total - money;
        
        if (answer <= 0) {
            answer = 0;
        }

        return answer;
    }
}
