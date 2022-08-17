import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        int[] report_cnt = new int[id_list.length];
        
        HashSet<String> hashSet = new HashSet<String>(Arrays.asList(report));
        String[] resultArr = hashSet.toArray(new String[0]);
        
        String[] id_cnt = new String[report.length];
        String[] id_report = new String[report.length];
        
        for (int i = 0; i < resultArr.length; i++){
            String[] tmp = resultArr[i].split(" ");
            id_cnt[i] = tmp[0];
            id_report[i] = tmp[1];
            for (int j = 0; j < id_list.length; j++){
                if (id_list[j].equals(id_report[i])){
                    report_cnt[j] += 1;
                }
            }
        }
        String[] report_list = new String[id_list.length];
        for (int i = 0; i < report_cnt.length; i++){
            if (report_cnt[i] >= k){
                report_list[i] = id_list[i];
            }
        }
        for (int i = 0; i < report_list.length; i++){
            for (int j = 0; j < resultArr.length; j++){
                if (id_report[j].equals(report_list[i])){
                    for (int l = 0; l < id_list.length; l++){
                        if (id_cnt[j].equals(id_list[l])){
                            answer[l] += 1;
                        }
                    }
                }
            }
        }
        return answer;
    }
}
