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
        _, _, ret, _ = self.f(root, None, 0, [], 0)
        return ret

    def f(self, root, preval, precnt, maxvals, maxcnt):
        if not root:
            return None, 0, [], 0
        if root.left:
            preval, precnt, maxvals, maxcnt = self.f(root.left, preval, precnt, maxvals, maxcnt)
        val = root.val
        if val == preval:
            cnt = precnt + 1
        else:
            cnt = 1
        if maxcnt < cnt:
            maxvals = [root.val]
            maxcnt = cnt
        elif maxcnt == cnt:
            maxvals.append(root.val)
        if root.right:
            val, cnt, maxvals, maxcnt = self.f(root.right, val, cnt, maxvals, maxcnt)
        return val, cnt, maxvals, maxcnt
                
            
        

# @lc code=end

