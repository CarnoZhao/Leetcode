#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a = '0' * (maxlen - len(a)) + a
        b = '0' * (maxlen - len(b)) + b
        ret = ''
        up = '0'
        for i in range(maxlen - 1, -1, -1):
            if a[i] == b[i]:
                ret = up + ret
                up = a[i]
            else:
                ret = ('0' if up == '1' else '1') + ret
        if up == '1':
            return up + ret
        else:
            return ret

# @lc code=end

