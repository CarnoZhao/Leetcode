/*
 * @Author: Xun Zhao
 * @Date: 2019-09-21 16:29:00
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-21 16:41:36
 * @Description: 
 */

/*
 * @lc app=leetcode.cn id=69 lang=java
 *
 * [69] x 的平方根
 */
class Solution {
    public int mySqrt(int x) {
        long l = 1;
        long r = x;
        long mid;
        long diff;
        while (r - l > 1) {
            mid = (l + r) / 2;
            diff = x - mid * mid;
            if (diff > 0) {
                l = mid;
            } else if (diff == 0) {
                return (int)mid;
            } else {
                r = mid;
            }
        }
        return (int)(l + r) / 2;
    }
}

