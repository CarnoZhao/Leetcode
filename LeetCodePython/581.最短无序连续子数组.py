#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mx = [-2 ** 32]
        mn = [2 ** 31 - 1]
        for n in nums:
            mx.append(max(mx[-1], n))
        for n in nums[::-1]:
            mn.append(min(mn[-1], n))
        cnt = len(nums)
        for i in range(len(nums)):
            if mx[1 + i] <= mn[-i - 1]:
                cnt -= 1
            else:
                break
        for j in range(len(nums) - 1, i, -1):
            if mx[j + 1] <= mn[-j - 1]:
                cnt -= 1
            else:
                break
        return cnt

# @lc code=end

