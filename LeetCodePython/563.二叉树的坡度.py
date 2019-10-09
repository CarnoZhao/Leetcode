#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        _, ret = self.f(root)
        return ret
        
    def f(self, root):
        if not root:
            return 0, 0
        if root.left:
            ls, ld = self.f(root.left)
        else:
            ls = ld = 0
        if root.right:
            rs, rd = self.f(root.right)
        else:
            rs = rd = 0
        d = ld + rd + abs(ls - rs)
        s = ls + rs + root.val
        return s, d
# @lc code=end

