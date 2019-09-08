/*
 * @lc app=leetcode.cn id=67 lang=java
 *
 * [67] 二进制求和
 */
class Solution {
    public String addBinary(String a, String b) {
        boolean up = false;
        String ret = "";
        char ac;
        char bc;
        for (int i = 0; i < Math.max(a.length(), b.length()); i ++) {
            if (i < a.length()) {
                ac = a.charAt(a.length() - i - 1);
            } else {
                ac = '0';
            }
            if (i < b.length()) {
                bc = b.charAt(b.length() - i - 1);
            } else {
                bc = '0';
            }
            if (ac != bc) {
                ret = (up ? "0" : "1") + ret;
            } else {
                ret = (up ? "1" : "0") + ret;
                up = ac == '1';
            }
        }
        return (up ? "1" : "") + ret;
    }
}

