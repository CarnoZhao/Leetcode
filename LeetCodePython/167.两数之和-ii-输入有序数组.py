#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            subtar = target - num
            l = i + 1
            r = len(numbers) - 1
            while r - l > 1:
                m = (l + r) // 2
                if numbers[m] > subtar:
                    r = m
                elif numbers[m] < subtar:
                    l = m
                else:
                    return [i + 1, m + 1]
            if numbers[l] == subtar:
                return [i + 1, l + 1]
            elif numbers[r] == subtar:
                return [i + 1, r + 1]

# @lc code=end

