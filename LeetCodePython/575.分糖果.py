#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        dic = {}
        for c in candies:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        b = 0
        s = 0
        for v in dic.values():
            if v >= 2:
                s += 1
                b += v - 1
            elif b >= s:
                s += v
            else:
                b += v
        return s
# @lc code=end

