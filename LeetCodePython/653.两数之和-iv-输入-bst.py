#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        st = [root]
        dic = {}
        ret = False
        while st:
            r = st.pop()
            if r.right:
                st.append(r.right)
            if r.left:
                st.append(r.left)
            if r.val in dic:
                ret = True
                break
            else:
                dic[k - r.val] = r.val
        return ret

# @lc code=end

