#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            ret *= 10
            ret += (x % 10)
            x //= 10
        ret *= sign
        if not -2 ** 31 <= ret <= 2 ** 31 - 1:
            return 0
        else:
            return ret
# @lc code=end

