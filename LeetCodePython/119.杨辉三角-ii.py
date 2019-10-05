#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from math import factorial
        return [factorial(rowIndex) // (factorial(i) * factorial(rowIndex - i)) for i in range(rowIndex + 1)]
# @lc code=end

