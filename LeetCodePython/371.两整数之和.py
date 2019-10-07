#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a + b
        while b != 0:
            up = a & b
            up <<= 1
            a = a ^ b
            b = up
        return a
# @lc code=end

