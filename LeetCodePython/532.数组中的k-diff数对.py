#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = j = 0
        pre = None
        ret = 0
        while i < len(nums) and j < len(nums):
            x = nums[i]
            y = nums[j]
            if y - x == k and i != j:
                if (y, x) != pre:
                    ret += 1
                pre = (y, x)
                j += 1
                i += 1
            elif y - x < k or i == j:
                j += 1
            else:
                i += 1
        return ret
# @lc code=end

