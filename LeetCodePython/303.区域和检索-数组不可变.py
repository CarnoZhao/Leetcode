#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for num in nums:
            self.sums.append(num + self.sums[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

