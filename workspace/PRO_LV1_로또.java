import java.util.*;
class Solution {
    public static int[] solution(int[] lottos, int[] win_nums) {
        int cnt = 0;
        int zero = 0;
        for (int i=0; i<lottos.length; i++){
            if(lottos[i] == 0){
                zero += 1;
                continue;
            }
            for (int j=0; j<win_nums.length; j++){
                if (lottos[i] == win_nums[j]) {
                    cnt += 1;
                    break;
                }
            }
        }
        int max = 7 - (cnt+zero);
        int min = 7 - (cnt);
        if (max == 7) max = 6;
        if (min == 7) min = 6;
        int[] answer = {max, min};
        return answer;
    }
    public static void main(String[] args){
        int[] lottos;
        int[] win_nums;

        Scanner sc = new Scanner(System.in);
        String tmp = sc.next();
        lottos = Arrays.stream(tmp.split(",")).mapToInt(Integer::parseInt).toArray();
        tmp = sc.next();
        win_nums = Arrays.stream(tmp.split(",")).mapToInt(Integer::parseInt).toArray();

        int[] result = solution(lottos, win_nums);
        System.out.println(result);
    }
}
