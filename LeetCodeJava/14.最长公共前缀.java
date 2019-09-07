/*
 * @lc app=leetcode.cn id=14 lang=java
 *
 * [14] 最长公共前缀
 */
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        String ret = "";
        char c;
        boolean fit = true;
        boolean len = true;
        for (int i = 0; i < strs[0].length(); i ++) {
            c = strs[0].charAt(i);
            for (String str : strs) {
                if (str.equals("")) {
                    fit = false;
                    break;
                } else if (c != str.charAt(i)) {
                    fit = false;
                    break;
                } else if (i == str.length() - 1) {
                    len = false;
                }
            }
            if (fit && len) {
                ret += c;
            } else if (fit && !len) {
                ret += c;
                break;
            } else {
                break;
            }
        }
        return ret;
    }
}

