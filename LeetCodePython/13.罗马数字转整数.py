#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        pre = None
        for char in s:
            if pre == None or values[pre] >= values[char]:
                ret += values[char]
            else:
                ret += values[char] - 2 * values[pre]
            pre = char
        return ret
# @lc code=end

