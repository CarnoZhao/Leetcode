/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */
class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) {
            return 0;
        }
        int j = 0;
        for (int i = 0; i < nums.length; i ++) {
            if (nums[i] != val) {
                nums[j] = nums[i];
                j ++;
            }
        }
        return j;
    }
}

