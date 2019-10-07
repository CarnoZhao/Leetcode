#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if not ('a' <= s[i] <= 'z' or '0' <= s[i] <= '9'):
                i += 1
            elif not ('a' <= s[j] <= 'z' or '0' <= s[j] <= '9'):
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
# @lc code=end

