#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        ret = []
        for i, num in enumerate(nums):
            if num > 0:
                ret.append(i + 1)
        return ret
# @lc code=end

