#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        return self.f(root, target, False)

    def f(self, root, target, start):
        if not root:
            return 0
        ret = int(root.val == target)
        if root.left:
            ret += self.f(root.left, target - root.val, True)
            if not start:
                ret += self.f(root.left, target, False)
        if root.right:
            ret += self.f(root.right, target - root.val, True)
            if not start:
                ret += self.f(root.right, target, False)
        return ret
             
# @lc code=end

