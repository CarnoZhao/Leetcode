#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        x = len(nums)
        y = len(nums[0])
        if x * y != r * c:
            return nums
        ret = [[0 for i in range(c)] for j in range(r)]
        for i in range(x):
            for j in range(y):
                z = i * y + j
                m = z // c
                n = z % c
                ret[m][n] = nums[i][j]
        return ret
# @lc code=end

