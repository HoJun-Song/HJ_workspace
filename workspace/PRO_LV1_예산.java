import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int max_money = 0;
        Arrays.sort(d);
        for (int i = 0; i < d.length; i++){
            max_money += d[i];
            if (max_money > budget) {
                break;
            }
            answer += 1;
        }
        return answer;
    }
}
