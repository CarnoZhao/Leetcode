/*
 * @lc app=leetcode.cn id=69 lang=java
 *
 * [69] x 的平方根
 */
class Solution {
    public int mySqrt(int x) {
        int l = 1;
        int r = x;
        int m;
        while (r - l > 1) {
            m = (l + r) / 2;
            if (m * m < x) {
                l = m;
            } else if (m * m > x) {
                r = m;
            } else {
                break;
            }
        }
        return l;
    }
}

