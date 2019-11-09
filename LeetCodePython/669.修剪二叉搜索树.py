#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)
        if root.val < L:
            root = right
        elif root.val > R:
            root = left
        else:
            root.left = left
            root.right = right
        return root 
# @lc code=end

