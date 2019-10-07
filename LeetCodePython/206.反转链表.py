#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ret, _ = self.f(head)
        return ret

    def f(self, head):
        if not head:
            return None, None
        elif not head.next:
            return head, head
        prehead, pretail = self.f(head.next)
        pretail.next = head
        head.next = None
        return prehead, head
# @lc code=end

