#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        a, b = None, None
        st = [root]
        while st:
            node = st.pop()
            if not node.left and not node.right:
                if node.val in (a, b):
                    continue
                elif a is None or node.val < a:
                    a, b = node.val, a
                elif b is None or a < node.val < b:
                    b = node.val
            else:
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
        return b if b is not None else -1


# @lc code=end

