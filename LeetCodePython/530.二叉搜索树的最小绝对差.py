#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        _, ret = self.f(root, None, 2 ** 32 - 1)
        return ret
        
    def f(self, root, preval, premindiff):
        if root.left:
            preval, premindiff = self.f(root.left, preval, premindiff)
        val = root.val
        if preval == None:
            mindiff = premindiff
        else:
            mindiff = min(premindiff, val - preval)
        if root.right:
            val, mindiff = self.f(root.right, val, mindiff)
        return val, mindiff
# @lc code=end

