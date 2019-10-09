#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            sig = '-'
        else:
            sig = ""
        ret = ""
        num= abs(num)
        while num != 0:
            ret = str(num % 7) + ret
            num //= 7
        return sig + ret
# @lc code=end

