#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        ret = [True for i in range(n - 1)]
        for i in range(2, n):
            if not ret[i - 1]:
                continue
            for j in range(2 * i, n, i):
                ret[j - 1] = False
        return sum(ret) - (n > 1)
# @lc code=end

