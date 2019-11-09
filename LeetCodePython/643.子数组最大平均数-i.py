#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = -k * 10000
        for i in range(len(nums) - k + 1):
            if i == 0:
                s = sum(nums[:k])
            else:
                s += nums[i + k - 1] - nums[i - 1]
            m = max(m, s)
        return m / k

# @lc code=end

