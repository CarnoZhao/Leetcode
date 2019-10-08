#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = 0
        j = 0
        ret = 0
        while i < len(houses) and j < len(heaters):
            s = houses[i]
            x = heaters[j]
            y = heaters[j - 1] if j != 0 else x
            if s < y:
                r = y - s
                ret = max(ret, r)
                i += 1
            elif y <= s <= x:
                r = min(x - s, s - y)
                ret = max(ret, r)
                i += 1
            elif j < len(heaters) - 1:
                j += 1
            else:
                r = s - x
                ret = max(ret, r)
                i += 1
        return ret
# @lc code=end

