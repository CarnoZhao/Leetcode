#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        lneedle = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + lneedle] == needle:
                return i
        return -1

# @lc code=end

