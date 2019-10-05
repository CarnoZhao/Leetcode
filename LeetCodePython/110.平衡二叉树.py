#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, ret = self.depthBalan(root)
        return ret

    def depthBalan(self, root):
        if root == None:
            return 0, True
        else:
            ld, lb = self.depthBalan(root.left)
            rd, rb = self.depthBalan(root.right)
            depth = max(ld, rd) + 1
            balan = lb and rb and abs(ld - rd) <= 1
            return depth, balan
# @lc code=end

