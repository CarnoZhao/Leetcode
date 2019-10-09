#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret = ""
        rem = len(s) % (2 * k)
        cyc = len(s) // (2 * k)
        if rem != 0:
            cyc += 1
        for i in range(cyc):
            start = 2 * i * k
            end = 2 * (i + 1) * k if i != cyc - 1 else len(s)
            for j in range(min(k, end - start)):
                ret += s[start + min(k, end - start) - j - 1]
            for j in range(min(k, end - start - k)):
                ret += s[start + k + j]
        return ret
# @lc code=end

