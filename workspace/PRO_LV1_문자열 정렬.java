import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings);
        
        for(int i = 1; i < strings.length; i++) {
			for(int j = 0; j < strings.length - i; j++) {
                char target = strings[j].charAt(n);
                char cmp = strings[j + 1].charAt(n);
				if(target > cmp) {
					swap(strings, j, j + 1);
				}
			}
		}
        
        String[] answer = strings;
        return answer;
    }
    
    private static void swap(String[] a, int i, int j) {
		String tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}
}
