#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m = c = 0
        pre = None
        for n in nums:
            if pre == None or n > pre:
                c += 1
            else:
                c = 1
            pre = n
            m = max(m, c)
        return max(m, c)

# @lc code=end

