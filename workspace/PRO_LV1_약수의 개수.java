class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        for (int i = left; i <= right; i++){
            int sign = 1;
            if (getNum(i) % 2 == 1){
                sign = -1;
            }
            answer += i * sign;
        }
        return answer;
    }
    
    public int getNum(int num){
        int count = 0;
        for (int i = 1; i <= num; i++){
            if (num % i == 0){
                count++;
            }
        }
        return count;
    }
}
