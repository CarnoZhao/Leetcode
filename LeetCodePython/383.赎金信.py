#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = self.count(ransomNote)
        dic2 = self.count(magazine)
        for key in dic1:
            if key not in dic2 or dic2[key] < dic1[key]:
                return False
        return True
        
    def count(self, s):
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        return dic
    
# @lc code=end

