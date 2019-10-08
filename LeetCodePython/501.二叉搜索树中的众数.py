#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

    def f(self, root, preval, precnt, premaxcnt):
        val = root.val
        cnt = 1 if val != preval else preval + 1
        maxcnt = max(premaxcnt)
        if root.left:
            lval, lcnt, lmaxcnt = self.f(root.left)
            if lval == val:
                cnt += lcnt
                maxcnt = max(lmaxcnt, cnt)
        if root.right:
            rval, rcnt, rmaxcnt = self.f(root.right)
            
        

# @lc code=end

