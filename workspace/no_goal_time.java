import java.util.Arrays;
public class no_goal_time {
	public String solution(String[] participant, String[] completion) {
		String tmp = "";
		int flag = 0;
		Arrays.sort(participant, String.CASE_INSENSITIVE_ORDER);
		Arrays.sort(completion, String.CASE_INSENSITIVE_ORDER);
		for (int i=0; i<completion.length; i++) {
			if (!(completion[i].equals(participant[i]))) {
				flag = 1;
				tmp = participant[i];
				break;
			}
		}
		String answer = "";
		if (flag == 0) {
			answer = participant[participant.length - 1];
		}
		else {
			answer = tmp;
		}
        return answer;
    }
}