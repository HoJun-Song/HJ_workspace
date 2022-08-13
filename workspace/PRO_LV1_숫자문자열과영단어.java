import java.util.*;
class Solution {
    public int solution(String s) {
        ArrayList<Integer> sol = new ArrayList<Integer>();
        String tmp = "";
        for (int i = 0; i < s.length(); i++) {
            int num = s.charAt(i) - '0';
            if (tmp.length() == 2) {
                char firstWord = tmp.charAt(0);
                if (firstWord == 'z') {
                    i += 1;
                    sol.add(0);
                }
                else if (firstWord == 'o') {
                    sol.add(1);
                }
                else if (firstWord == 'e') {
                    i += 2;
                    sol.add(8);
                }
                else if (firstWord == 'n') {
                    i += 1;
                    sol.add(9);
                }
                else {
                    char secondWord = tmp.charAt(1);
                    if (firstWord == 't') {
                        if (secondWord == 'w') {
                            sol.add(2);
                        }
                        else {
                            i += 2;
                            sol.add(3);
                        }
                    }
                    else if (firstWord == 'f') {
                        if (secondWord == 'o') {
                            i += 1;
                            sol.add(4);
                        }
                        else {
                            i += 1;
                            sol.add(5);
                        }
                    }
                    else {
                        if (secondWord == 'i') {
                            sol.add(6);
                        }
                        else {
                            i += 2;
                            sol.add(7);
                        }
                    }
                }
                tmp = "";
            }
            else if (num >= 0 && num <= 9) {
                tmp = "";
                sol.add(num);
            }
            else {
                tmp += s.charAt(i);
            }
        }
        String answerTmp = sol.toString().replaceAll("[^0-9]","");
        int answer = Integer.parseInt(answerTmp);
        return answer;
    }
}
