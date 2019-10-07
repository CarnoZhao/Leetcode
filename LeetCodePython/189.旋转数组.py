#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        if k == 0:
            return None
        cyc = self.gcd(length, k)
        sublen = length // cyc
        for i in range(cyc):
            tmp = None
            for j in range(sublen + 1):
                idx = (i + j * k) % length
                nums[idx], tmp = tmp, nums[idx]

    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

# @lc code=end

