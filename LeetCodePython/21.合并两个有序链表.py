#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        else:
            ret = ListNode(0)
            head = ret
            while l1 != None or l2 != None:
                if l1 == None:
                    head.next = l2
                    l2 = l2.next
                elif l2 == None:
                    head.next = l1
                    l1 = l1.next
                elif l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            return ret.next

# @lc code=end

