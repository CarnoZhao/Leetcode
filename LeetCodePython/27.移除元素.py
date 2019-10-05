#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        j = 0
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
        return j
# @lc code=end

