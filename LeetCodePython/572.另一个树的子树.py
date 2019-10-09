#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ret = self.f(s, t, False)
        return ret


    def f(self, s, t, start):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        ret = s.val == t.val
        if ret:
            ret = self.f(s.left, t.left, True) and self.f(s.right, t.right, True)
        if not start:
            ret = ret or self.f(s.left, t, False) or self.f(s.right, t, False)
        return ret

            

# @lc code=end

