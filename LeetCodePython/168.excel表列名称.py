#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ""
        while n != 0:
            n -= 1
            a = n % 26
            n //= 26
            ret = chr(ord("A") + a) + ret
        return ret

# @lc code=end

