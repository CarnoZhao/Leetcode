#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            result = m * (m + 1) // 2
            if result > n:
                r = m
            else:
                l = m + 1
        return l - 1
            
            
# @lc code=end

