import java.util.*;
public class sum_two {
	public int[] solution(int[] numbers) {
        HashSet<Integer> tmp = new HashSet<>();
        for (int i=0; i<numbers.length; i++) {
        	for (int j=i+1; j<numbers.length; j++) {
        		int sum = numbers[i] + numbers[j];
        		tmp.add(sum);
        	}
        }
        int[] answer = new int[tmp.size()];
        int idx = 0;
        for (int val: tmp) {
        	answer[idx] = val;
        	idx++;
        }
        Arrays.sort(answer);
        return answer;
    }
}