#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                ret = max(cnt, ret)
                cnt = 0
        ret = max(cnt, ret)
        return ret
# @lc code=end

