#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)
        dic = {}
        revdic = {}
        for i in range(length):
            a, b = s[i], t[i]
            if (a in dic and b != dic[a]) or (b in revdic and a != revdic[b]):
                return False
            elif (a not in dic) or (b not in revdic):
                dic[a] = b
                revdic[b] = a
        return True
# @lc code=end

