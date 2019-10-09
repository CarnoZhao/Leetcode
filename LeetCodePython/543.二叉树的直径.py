#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, ret = self.f(root)
        return ret

    def f(self, root):
        if not root:
            return 0, 0
        ldp, ldm = self.f(root.left)
        rdp, rdm = self.f(root.right)
        dp = max(ldp, rdp) + 1
        dm = max(ldm, rdm, ldp + rdp)
        return dp, dm
# @lc code=end

