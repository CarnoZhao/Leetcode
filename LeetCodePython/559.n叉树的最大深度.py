#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
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
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        dps = [self.maxDepth(c) for c in root.children]
        if not dps:
            maxdp = 0
        else:
            maxdp = max(dps)
        return maxdp + 1

# @lc code=end

