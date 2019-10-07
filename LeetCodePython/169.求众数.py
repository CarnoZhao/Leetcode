#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ref = 0
        cnt = 0
        for num in nums:
            if cnt == 0:
                ref = num
                cnt += 1
            elif num == ref:
                cnt += 1
            elif num != ref:
                cnt -= 1
        return ref
# @lc code=end

