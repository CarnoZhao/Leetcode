#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        if len(pattern) != len(string.split()):
            return False
        dic = {}
        rdic = {}
        for c, word in zip(pattern, string.split()):
            if c not in dic and word not in rdic:
                dic[c] = word
                rdic[word] = c
            elif (c in dic and dic[c] != word) or (word in rdic and rdic[word] != c):
                return False
        return True
# @lc code=end

