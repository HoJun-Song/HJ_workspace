import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int max = nums.length / 2;
        int answer = 0;
        
        Set<Integer> set = new HashSet<Integer>();
		for(int i : nums)
			set.add(i);
		
		List<Integer> list = new ArrayList<Integer>(set);
        
        if (max <= list.size()){
            answer = max;
        }
        else{
            answer = list.size();
        }

        return answer;
    }
}