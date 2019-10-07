#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while i < len(nums):
            if nums[j] != 0:
                j += 1
                i = j
            elif nums[i] == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1

# @lc code=end

