#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        roots = [root]
        ret = []
        while roots:
            tmp = []
            add = []
            for root in roots:
                add.append(root.val)
                for c in root.children:
                    if c:
                        tmp.append(c)
            roots = tmp
            ret.append(add)
        return ret
# @lc code=end

