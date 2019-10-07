#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret = 0
        for p1 in points:
            dic = {}
            for p2 in points:
                dist = self.dist(p1, p2)
                if dist not in dic:
                    dic[dist] = 1
                else:
                    dic[dist] += 1
            for v in dic.values():
                ret += v * (v - 1)
        return ret
        

    def dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

# @lc code=end

