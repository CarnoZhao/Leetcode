#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in "aeiouAEIOU":
                i += 1
                continue
            if s[j] not in "aeiouAEIOU":
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        s = "".join(s)
        return s
            
# @lc code=end

