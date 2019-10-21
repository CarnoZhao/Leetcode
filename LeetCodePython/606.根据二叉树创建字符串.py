#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        ret = str(t.val)
        if t.left and t.right:
            return ret + "(%s)(%s)" % (self.tree2str(t.left), self.tree2str(t.right))
        elif t.left and not t.right:
            return ret + "(%s)" % self.tree2str(t.left)
        elif not t.left and t.right:
            return ret + "()(%s)" % self.tree2str(t.right)
        else:
            return ret
# @lc code=end

