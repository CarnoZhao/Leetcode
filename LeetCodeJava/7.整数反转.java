/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */
class Solution {
    public int reverse(int x) {
        long ret = 0;
        int sign = Integer.signum(x);
        x = Math.abs(x);
        while (x != 0) {
            ret *= 10;
            ret += x % 10;
            x /= 10;
        }
        ret *= sign;
        if (ret < Integer.MIN_VALUE || ret > Integer.MAX_VALUE) {
            return 0;
        } else {
            return (int) (ret);
        }
    }
}

