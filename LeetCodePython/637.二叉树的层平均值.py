#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ret = []
        roots = [root]
        while roots:
            tmp = []
            s = 0
            cnt = 0
            for root in roots:
                s += root.val
                if root.left:
                    tmp.append(root.left)
                if root.right:
                    tmp.append(root.right)
                cnt += 1
            roots = tmp
            ret.append(s / cnt)
        return ret
# @lc code=end

