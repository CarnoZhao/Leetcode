#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        paths = []
        if root.left:
            for subp in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + subp)
        if root.right:
            for subp in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + subp)
        return paths


# @lc code=end

