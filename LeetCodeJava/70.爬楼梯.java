/*
 * @Author: Xun Zhao
 * @Date: 2019-09-21 16:43:40
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-21 16:46:36
 * @Description: 
 */
/*
 * @lc app=leetcode.cn id=70 lang=java
 *
 * [70] 爬楼梯
 */
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < n + 1; i ++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}

