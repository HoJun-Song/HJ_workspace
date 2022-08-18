import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        Arrays.sort(arr);
        List<Integer> tmp = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor == 0) {
                tmp.add(arr[i]);
            }
        }
        if (tmp.size() == 0) {
            tmp.add(-1);
        }
        int[] answer = tmp.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}
