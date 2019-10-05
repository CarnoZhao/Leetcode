#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        roots = [root]
        while roots:
            ret.append([root.val for root in roots])
            tmp = []
            for root in roots:
                if root == None:
                    continue
                if root.left != None:
                    tmp.append(root.left)
                if root.right != None:
                    tmp.append(root.right)
            roots = tmp
        return ret[::-1]
# @lc code=end

