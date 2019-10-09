#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        m = int(num ** 0.5)
        ret = 1
        for i in range(2, m + 1):
            j = num // i
            if i * j == num:
                if i != j:
                    ret += i + j
                else:
                    ret += i
        return ret == num

# @lc code=end

