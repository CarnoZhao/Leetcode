#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in '([{':
                ls.append(char)
            elif ls and ls[-1] == dic[char]:
                ls.pop()
            else:
                return False
        return ls == []
# @lc code=end

