#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre = None
        j = 0
        for i, num in enumerate(nums):
            if i != 0 and num != pre:
                j += 1
                nums[j] = num
            pre = num
        return j + 1
                
# @lc code=end

