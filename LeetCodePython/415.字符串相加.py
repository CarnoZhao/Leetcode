#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = -1
        j = -1
        ret = ""
        up = 0
        while i >= -len(num1) or j >= -len(num2):
            if i < -len(num1):
                c1 = "0"
            else:
                c1 = num1[i]
            if j < -len(num2):
                c2 = "0"
            else:
                c2 = num2[j]
            add = ord(c1) + ord(c2) - 2 * ord('0') + up
            up = add // 10
            add %= 10
            ret = chr(add + ord('0')) + ret
            i -= 1
            j -= 1
        if up == 1:
            ret = "1" + ret
        return ret

# @lc code=end

