/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */
class Solution {
    public boolean isPalindrome(int x) {
        String str = x + "";
        String rev;
        rev = new StringBuilder(str).reverse().toString();
        return str.equals(rev);
    }
}

