function solution(s) {
    var answer = true;
    if (s.length != 4 && s.length != 6) {
        answer = false;
    }
    for (var i = 0; i < s.length; i++) {
        if (s[i] < '0' || s[i] > '9') {
            answer = false;
        }
    }
    return answer;
}
