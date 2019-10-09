#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        if N == 0:
            return 0
        for i in range(N - 1):
            a, b = b, a + b
        return b
# @lc code=end

