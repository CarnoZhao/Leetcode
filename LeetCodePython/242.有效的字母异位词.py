#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        for c in t:
            if c not in dic:
                return False
            else:
                dic[c] -= 1
        return all([v == 0 for v in dic.values()])
# @lc code=end

