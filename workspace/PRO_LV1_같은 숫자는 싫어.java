import java.util.*;
public class Solution {
    public int[] solution(int[] arr) {
        List<Integer> myclass = new ArrayList<>();
        myclass.add(arr[0]);
        int cnt = 0;
        
        for (int i = 1; i < arr.length; i++) {
            int tmp = myclass.get(cnt);
            
            if (tmp != arr[i]) {
                myclass.add(arr[i]);
                cnt++;
            }
            else {
                continue;
            }
            
        }
        
        int[] answer = myclass.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}
