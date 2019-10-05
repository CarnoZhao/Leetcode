#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split()
        if len(sp) == 0:
            return 0
        else:
            return len(sp[-1])
# @lc code=end

