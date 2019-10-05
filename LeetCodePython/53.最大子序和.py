#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]
        for num in nums:
            dp.append(max(num, dp[-1] + num))
        return max(dp[1:])
# @lc code=end

