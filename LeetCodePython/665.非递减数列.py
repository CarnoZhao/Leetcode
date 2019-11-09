#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums) - 1):
            pre, post = nums[i:i + 2]
            if post < pre:
                if i == 0 or post > nums[i - 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                cnt += 1
        return cnt <= 1
# @lc code=end

