import java.util.Arrays;

/*
 * @Author: Xun Zhao
 * @Date: 2019-09-21 17:03:28
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-22 14:47:12
 * @Description: 
 */
/*
 * @lc app=leetcode.cn id=88 lang=java
 *
 * [88] 合并两个有序数组
 */
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tmp = new int[m + n];
        int i = 0;
        int j = 0;
        for (int k = 0; k < m + n; k ++) {
            if (i >= m && j < n) {
                tmp[k] = nums2[j];
                j ++;
            } else if (i < m && j >= n) {
                tmp[k] = nums1[i];
                i ++;
            } else if (nums1[i] <= nums2[j]) {
                tmp[k] = nums1[i];
                i ++;
            } else {
                tmp[k] = nums2[j];
                j ++;
            }
        }
        for (int k = 0; k < m + n; k ++) {
            nums1[k] = tmp[k];
        }
    }
}

