class Solution {
    fun solution(arr: IntArray): IntArray {
        var min = arr[0]
        for (i in arr.indices) {
            if (arr[i] < min) {
                min = arr[i]
            }
        }
        val error: IntArray = intArrayOf(-1)
        var answer = arr.filter {it != min}.toIntArray()
        if (answer.size == 0) return error
        return answer
    }
}