#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            add = [1 if j == 0 or j == i else ret[-1][j - 1] + ret[-1][j] for j in range(i + 1)]
            ret.append(add)
        return ret
# @lc code=end

