/*
 * @lc app=leetcode.cn id=69 lang=java
 *
 * [69] x 的平方根
 */
class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        } else if (x < 4) {
            return 1;
        } else if (x < 9) {
            return 3;
        }
        int l = 0;
        int r = x / 2;
        int m;
        while (r - l > 1) {
            m = (l + r) / 2;
            if (m * m < x) {
                l = m;
            } else if (m * m > x) {
                r = m;
            } else {
                return m;
            }
        }
        return l;
    }
}

