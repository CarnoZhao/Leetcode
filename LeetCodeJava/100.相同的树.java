/*
 * @Author: Xun Zhao
 * @Date: 2019-09-22 14:47:25
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-22 14:57:15
 * @Description: 
 */
/*
 * @lc app=leetcode.cn id=100 lang=java
 *
 * [100] 相同的树
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p == null || q == null) {
            return false;
        } else {
            return (p.val == q.val) && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
    }
}

