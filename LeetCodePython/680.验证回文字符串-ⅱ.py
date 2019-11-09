#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        i = 0; j = len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i < j:
            return s[i:j] == s[i:j][::-1] or s[i + 1:j + 1] == s[i + 1:j + 1][::-1]
        else:
            return True
# @lc code=end

