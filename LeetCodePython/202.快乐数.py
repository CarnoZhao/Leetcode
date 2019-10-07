#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        return self.f(n, set())

    def f(self, n, his):
        if n == 1:
            return True
        ret = 0
        while n != 0:
            ret += (n % 10) ** 2
            n //= 10
        if ret in his:
            return False
        else:
            his.add(ret)
            return self.f(ret, his)
# @lc code=end

