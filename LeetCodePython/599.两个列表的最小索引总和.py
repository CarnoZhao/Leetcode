#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for i, l in enumerate(list1):
            dic[l] = [i]
        for i, l in enumerate(list2):
            if l in dic:
                dic[l].append(i)
        cnt = 2 ** 32 - 1
        ret = []
        for key in dic:
            if len(dic[key]) == 2:
                if sum(dic[key]) < cnt:
                    ret = [key]
                    cnt = sum(dic[key])
                elif sum(dic[key]) == cnt:
                    ret.append(key)
        return ret
# @lc code=end

