#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        up = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += up
            if digits[i] >= 10:
                up = digits[i] // 10
                digits[i] %= 10
            else:
                up = 0
        if up != 0:
            return [1] + digits
        else:
            return digits 
# @lc code=end

