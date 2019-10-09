#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower():
            return True
        elif word[0] == word[0].upper() and word[1:].lower() == word[1:]:
            return True
        else:
            return False


# @lc code=end

