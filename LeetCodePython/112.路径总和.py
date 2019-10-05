#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        roots = [root]
        while roots:
            tmp = []
            for root in roots:
                if root.left == None and root.right == None:
                    if root.val == target:
                        return True
                else:
                    if root.left != None:
                        newroot = TreeNode(root.left.val + root.val)
                        newroot.left = root.left.left
                        newroot.right = root.left.right
                        tmp.append(newroot)
                    if root.right != None:
                        newroot = TreeNode(root.right.val + root.val)
                        newroot.left = root.right.left
                        newroot.right = root.right.right
                        tmp.append(newroot)
            roots = tmp
        return False
# @lc code=end

