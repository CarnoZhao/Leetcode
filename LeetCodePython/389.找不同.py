#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for c in s:
            ret ^= ord(c)
        for c in t:
            ret ^= ord(c)
        return chr(ret)
# @lc code=end

