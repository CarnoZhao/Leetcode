#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        ret = 0
        yes = False
        i = 0
        while i < len(s):
            if yes:
                if s[i] != ' ':
                    i += 1
                else:
                    yes = False
            else:
                if s[i] == ' ':
                    i += 1
                else:
                    ret += 1
                    yes = True
        return ret
# @lc code=end

