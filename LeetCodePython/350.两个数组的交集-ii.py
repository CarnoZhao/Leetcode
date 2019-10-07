#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        dic1 = self.count(nums1)
        dic2 = self.count(nums2)
        for key in dic1:
            if key in dic2:
                ret += [key] * min(dic1[key], dic2[key])
        return ret
        

    def count(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        return dic
# @lc code=end

