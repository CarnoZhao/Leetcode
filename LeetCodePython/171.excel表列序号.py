#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0
        for c in s:
            ret *= 26
            ret += ord(c) - ord('A') + 1
        return ret
# @lc code=end

