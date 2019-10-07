#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        length = len(s)
        dic = {}
        for i, c in enumerate(s):
            if c not in dic:
                dic[c] = i
            else:
                dic[c] = length
        ret = min(dic.values())
        if ret == length:
            return -1
        else:
            return ret
# @lc code=end

