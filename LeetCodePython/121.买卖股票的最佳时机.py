#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [(-2 ** 32, 0)]
        for num in prices:
            buy = max(-num, dp[-1][0])
            sell = max(num + dp[-1][0], dp[-1][-1])
            dp.append((buy, sell))
        return dp[-1][-1]
# @lc code=end

