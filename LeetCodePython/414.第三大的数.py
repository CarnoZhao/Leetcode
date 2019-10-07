#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f, s, t = -2 ** 32, -2 ** 32, -2 ** 32
        for num in nums:
            if num > f:
                f, s, t = num, f, s
            elif num == f:
                continue
            elif num > s:
                s, t = num, s
            elif num == s:
                continue
            elif num > t:
                t = num
        return t if t != -2 ** 32 else f

# @lc code=end

