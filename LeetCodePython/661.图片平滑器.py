#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        from itertools import product
        from copy import deepcopy
        ret = deepcopy(M)
        r = len(M); c = len(M[0])
        for i in range(r):
            for j in range(c):
                p = product((i - 1, i, i + 1), (j - 1, j, j + 1))
                s = 0; n = 0
                for x, y in p:
                    if 0 <= x < r and 0 <= y < c:
                        s += M[x][y]
                        n += 1
                ret[i][j] = int(s / n)
        return ret
                


# @lc code=end

