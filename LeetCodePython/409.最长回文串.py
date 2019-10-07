#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        ret = 0
        hasOdd = False
        for v in dic.values():
            if v % 2 == 0:
                ret += v
            else:
                ret += v - 1
                hasOdd = True
        ret += hasOdd
        return ret
# @lc code=end

