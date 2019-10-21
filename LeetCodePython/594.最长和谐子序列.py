#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        skeys = sorted(dic.keys())
        ret = 0
        for i in range(len(skeys) - 1):
            if skeys[i + 1] - skeys[i] > 1:
                continue
            ret = max(ret, dic[skeys[i]] + dic[skeys[i + 1]])
        return ret
# @lc code=end

