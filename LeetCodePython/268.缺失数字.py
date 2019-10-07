#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sums = l * (l + 1) // 2
        return sums - sum(nums)
# @lc code=end

