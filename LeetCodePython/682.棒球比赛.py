#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        import re
        st = []
        for o in ops:
            if re.compile("-?\d+").match(o):
                st.append(eval(o))
            elif o == '+':
                st.append(sum(st[-2:]))
            elif o == 'D':
                st.append(2 * st[-1])
            elif o == 'C':
                st.pop()
        return sum(st)

# @lc code=end

