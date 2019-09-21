/*
 * @Author: Xun Zhao
 * @Date: 2019-09-21 17:03:28
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-21 20:27:06
 * @Description: 
 */
/*
 * @lc app=leetcode.cn id=88 lang=java
 *
 * [88] 合并两个有序数组
 */
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0) {
            for (int i = 0; i < n; i ++) {
                nums1[i + m] = nums2[i];
            }
        } else if (n != 0) {
            int j = 0;
            int tmp;
            for (int i = 0; i < m; i ++) {
                if (nums1[i] > nums2[j]) {
                    tmp = nums1[i];
                    nums1[i] = nums2[j];
                    nums2[j] = tmp;
                    j ++;
                }
            }
            for (int i = 0; i < n; i ++) {
                nums1[i + m] = nums2[i];
            }
        }
        
    }
}

