#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
        if not q:
            rev = self.reverseList(p)
        elif not q.next:
            rev = self.reverseList(p.next)
        while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True
        
        
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

