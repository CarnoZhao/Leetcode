#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ret = False
        for i in range(c):
            target = c - i * i
            if target < 0:
                break
            l = 0
            r = target
            while l < r:
                m = (l + r) // 2
                diff = m * m - target
                if diff > 0:
                    r = m
                else:
                    l = m + 1
            ret = l * l == target
            if ret:
                break
        return ret
# @lc code=end

