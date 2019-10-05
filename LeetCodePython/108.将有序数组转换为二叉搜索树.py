#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid = len(nums) // 2
            ret = TreeNode(nums[mid])
            ret.left = self.sortedArrayToBST(nums[:mid])
            if mid + 1 == len(nums):
                ret.right = None
            else:
                ret.right = self.sortedArrayToBST(nums[mid + 1:])
            return ret
# @lc code=end

