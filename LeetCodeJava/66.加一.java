/*
 * @lc app=leetcode.cn id=66 lang=java
 *
 * [66] 加一
 */
class Solution {
    public int[] plusOne(int[] digits) {
        int up = 0;
        for (int i = digits.length - 1; i >= 0; i --) {
            if (i == digits.length - 1) {
                digits[i] ++;
            }
            digits[i] += up;
            up = digits[i] / 10;
            digits[i] %= 10;
        }
        int[] ret;
        if (up == 0) {
            ret = digits;
        } else {
            ret = new int[digits.length + 1];
            ret[0] = up;
            for (int i = 0; i < digits.length; i ++) {
                ret[i + 1] = digits[i];
            }
        }
        return ret;
    }
}

