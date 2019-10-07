#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = ListNode(0)
        ret = p
        while head != None:
            if head.val != val:
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        return ret.next
# @lc code=end

