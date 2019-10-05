#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(1, n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

# @lc code=end

