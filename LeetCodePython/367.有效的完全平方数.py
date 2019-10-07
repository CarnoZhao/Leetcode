#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l < r:
            m = l + (r - l) // 2
            if m * m > num:
                r = m
            elif m * m < num:
                l = m + 1
            else:
                return True
        return l * l == num
# @lc code=end

