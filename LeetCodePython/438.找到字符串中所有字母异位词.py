#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ls, lp = len(s), len(p)
        dic = {}
        for cp in p:
            if cp not in dic:
                dic[cp] = 1
            else:
                dic[cp] += 1
        for j in range(lp - 1):
            if s[j] in dic:
                dic[s[j]] -= 1
        ret = []
        for i in range(ls - lp + 1):
            if i != 0 and s[i - 1] in dic:
                dic[s[i - 1]] += 1
            if s[i + lp - 1] in dic:
                dic[s[i + lp - 1]] -= 1
            if all([x == 0 for x in dic.values()]):
                ret.append(i)
        return ret




# @lc code=end

