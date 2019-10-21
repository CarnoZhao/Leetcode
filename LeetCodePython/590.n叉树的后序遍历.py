#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        st = [root]
        ret = []
        while st:
            if st[-1].children and (not ret or (ret and ret[-1] != st[-1].children[-1])):
                st.extend(st[-1].children[::-1])
            else:
                p = st.pop()
                ret.append(p)
        return [i.val for i in ret]

# @lc code=end

