#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ret = False
        for i in range(c + 1):
            if i ** 2 > c:
                break
            diff = (c - i ** 2) ** 0.5
            ret = diff == int(diff)
            if ret:
                break
        return ret
# @lc code=end

