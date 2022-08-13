function solution(s){
    var answer = true;
    var pCheck = 0;
    var yCheck = 0;

    for (var i = 0; i < s.length; i++) {
        if (s[i] == 'p' || s[i] == 'P') {
            pCheck += 1;
        }
        else if (s[i] == 'y' || s[i] == 'Y') {
            yCheck += 1;
        }
    }
    
    if (pCheck != yCheck) {
        answer = false;
    }

    return answer;
}
