#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        ret = 0
        while num != 0:
            ret += num % 10
            num //= 10
        return self.addDigits(ret)
# @lc code=end

