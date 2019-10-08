#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        n = 2
        while n <= num:
            n *= 2
        return (n - 1) ^ num
# @lc code=end

