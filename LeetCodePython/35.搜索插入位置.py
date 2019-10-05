#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or nums[0] >= target:
            return 0
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (l + r) // 2
            mid = nums[m]
            if mid == target:
                return m
            elif mid < target:
                l = m
            else:
                r = m
        return r

        
# @lc code=end

