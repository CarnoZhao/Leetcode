#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(1, len(prices)):
            now, pre = prices[i], prices[i - 1]
            if now - pre > 0:
                ret += now - pre
        return ret

# @lc code=end

