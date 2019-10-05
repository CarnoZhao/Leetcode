/*
 * @Author: Xun Zhao
 * @Date: 2019-09-22 14:57:40
 * @LastEditors: Xun Zhao
 * @LastEditTime: 2019-09-22 14:57:40
 * @Description: 
 */
/*
 * @lc app=leetcode.cn id=101 lang=java
 *
 * [101] 对称二叉树
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
    public boolean isSymmetric(TreeNode root) {
        return isSymmetricV2(root, root);
    }

    private boolean isSymmetricV2(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return true;
        } else if (root1 != null && root2 != null) {
            return (root1.val == root2.val) && isSymmetricV2(root1.left, root2.right) && isSymmetricV2(root1.right, root2.left);
        } else {
            return false;
        }
    } 
}

