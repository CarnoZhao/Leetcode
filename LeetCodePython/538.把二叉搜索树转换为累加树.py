#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        ret, _ = self.f(root, 0)
        return ret
    
    def f(self, root, accu):
        if not root:
            return None, 0
        if root.right:
            newright, accu = self.f(root.right, accu)
            root.right = newright
        accu += root.val
        root.val = accu
        if root.left:
            newleft, accu = self.f(root.left, accu)
            root.left = newleft
        return root, accu
# @lc code=end

