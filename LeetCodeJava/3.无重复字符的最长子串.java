/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0;
        int j = 0;
        int ret = 0;
        while (i < s.length() && j < s.length()) {
            if (s.substring(i, j).contains(s.substring(j, j + 1))) {
                i += 1;
            } else {
                j += 1;
                ret = j - i > ret ? j - i : ret;
            }
        }
        return ret;
    }
}

