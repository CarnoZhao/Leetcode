/*
 * @lc app=leetcode.cn id=35 lang=java
 *
 * [35] 搜索插入位置
 */
class Solution {
    public int searchInsert(int[] nums, int target) {
        if (nums.length == 0) {
            return 0;
        }
        int l = 0;
        int r = nums.length - 1;
        int mid;
        while (r - l > 1) {
            mid = (l + r) / 2;
            if (nums[mid] < target) {
                l = mid;
            } else {
                r = mid;
            }
        }
        return target > nums[l] ? target <= nums[r] ? r : r + 1 : l;
    }
}

