#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        i = j = 0
        while i < m or j < n:
            if i >= m:
                tmp.append(nums2[j])
                j += 1
            elif j >= n:
                tmp.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        for k in range(m + n):
            nums1[k] = tmp[k]
# @lc code=end

