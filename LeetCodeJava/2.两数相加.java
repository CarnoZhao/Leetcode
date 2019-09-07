/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(0);
        ListNode nex = ret;
        int up = 0;
        int val;
        while (l1 != null || l2 != null || up != 0) {
            val = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + up;
            up = val / 10;
            val = val % 10;
            nex.next = new ListNode(val);
            nex = nex.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        return ret.next;
    }
}

