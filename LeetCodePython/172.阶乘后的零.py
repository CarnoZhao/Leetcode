#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        while n != 0:
            n //= 5
            ret += n
        return ret
# @lc code=end

