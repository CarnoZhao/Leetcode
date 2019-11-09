#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        tmp = [0] * len(nums) 
        for n in nums:
            tmp[n - 1] += n
        for i in range(len(tmp)):
            if tmp[i] == 0:
                miss = i + 1
            if tmp[i] == 2 * i + 2:
                rep = i + 1
        return [rep, miss]
# @lc code=end

