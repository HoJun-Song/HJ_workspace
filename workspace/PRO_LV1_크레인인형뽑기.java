import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> bucket = new ArrayList<Integer>();
        for (int i: moves) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][i - 1] != 0) {
                    int num = board[j][i - 1];
                    board[j][i - 1] = 0;
                    bucket.add(num);
                    break;
                }
            }
            if (bucket.size() > 1) {
                int tmp = bucket.get(0);
                for (int j = 1; j < bucket.size(); j++) {
                    if (tmp == bucket.get(j)) {
                        bucket.remove(j-1);
                        bucket.remove(j-1);
                        answer += 2;
                    }
                    else {
                        tmp = bucket.get(j);
                    }
                }
            }
        }
        return answer;
    }
}
