#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        sums = 0
        while n > sums:
            i += 1
            sums += (10 ** i - 10 ** (i - 1)) * i
        sums -= (10 ** i - 10 ** (i - 1)) * i
        n -= sums
        num = 10 ** (i - 1) + (n - 1) // i
        idx = (n - 1) % i
        return str(num)[idx]



# @lc code=end

