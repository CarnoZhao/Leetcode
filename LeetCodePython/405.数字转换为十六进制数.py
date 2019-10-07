#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2 ** 32
        elif num == 0:
            return "0"
        ret = ""
        while num != 0:
            add = num % 16
            if add >= 10:
                add = chr(ord('a') + add - 10)
            else:
                add = str(add)
            ret = add + ret
            num //= 16
        return ret
# @lc code=end

