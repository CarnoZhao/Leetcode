#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                ret += (i == 0) + (i == len(grid) - 1)
                if i != 0:
                    ret += grid[i - 1][j] == 0
                if i != len(grid) - 1:
                    ret += grid[i + 1][j] == 0
                ret += (j == 0) + (j == len(grid[0]) - 1)
                if j != 0:
                    ret += grid[i][j - 1] == 0
                if j != len(grid[0]) - 1:
                    ret += grid[i][j + 1] == 0
        return ret 
                

# @lc code=end

