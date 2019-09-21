/*
 * @Author: Xun Zhao
 * @Date: 2019-09-21 16:47:04
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-21 17:02:59
 * @Description: 
 */
/*
 * @lc app=leetcode.cn id=83 lang=java
 *
 * [83] 删除排序链表中的重复元素
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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode ret = head;
        ListNode nex = ret;
        int pre = ret.val;
        head = head.next;
        while (head != null) {
            if (head.val != pre) {
                nex.next = head;
                nex = nex.next;
                pre = head.val;
            }
            head = head.next;
        }
        nex.next = null;
        return ret;
    }
}

