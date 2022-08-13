import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] tmp = toThree(n);
        
        answer = toTen(tmp);
        
        return answer;
    }
    public int[] toThree(int num) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = num; i > 0; i /= 3) {
            arr.add(i % 3);
        }
        Collections.reverse(arr);
        int[] result = arr.stream().mapToInt(i -> i).toArray();
        return result;
    }
    public int toTen(int[] num) {
        int result = 0;
        int cnt = 1;
        for (int i = 0; i < num.length; i++) {
            result += num[i] * cnt;
            cnt *= 3;
        }
        return result;
    }
}
