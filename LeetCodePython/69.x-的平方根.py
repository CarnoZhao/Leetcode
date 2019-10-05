#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x
        l = 0
        r = x
        while r - l > 1:
            m = (l + r) // 2
            if m * m < x:
                l = m
            elif m * m > x:
                r = m
            else:
                return m
        return l
# @lc code=end

