#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        order = sorted(nums, reverse = True)
        dic = dict((o, i + 1) for i, o in enumerate(order))
        ret = []
        for num in nums:
            r = dic[num]
            if r == 1:
                r = "Gold Medal"
            elif r == 2:
                r = "Silver Medal"
            elif r == 3:
                r = "Bronze Medal"
            else:
                r = str(r)
            ret.append(r)
        return ret
# @lc code=end

