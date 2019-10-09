#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ret = []
        st = [root]
        while st:
            root = st.pop()
            ret.append(root.val)
            st.extend(root.children[::-1])
        return ret
# @lc code=end

