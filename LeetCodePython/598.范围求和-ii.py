#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([m] + [op[0] for op in ops]) * min([n] + [op[1] for op in ops])
# @lc code=end

