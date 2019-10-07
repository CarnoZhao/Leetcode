#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = (0, 0)
        for num in nums:
            yes = dp[1] + num
            no = max(dp)
            dp = (yes, no)
        return max(dp)
# @lc code=end

