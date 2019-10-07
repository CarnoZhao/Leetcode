#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and not (root.left.left or root.left.right):
            ret = root.left.val
            if root.right:
                ret += self.sumOfLeftLeaves(root.right)
            return ret
        else:
            ret = 0
            if root.left:
                ret += self.sumOfLeftLeaves(root.left)
            if root.right:
                ret += self.sumOfLeftLeaves(root.right)
            return ret
# @lc code=end

