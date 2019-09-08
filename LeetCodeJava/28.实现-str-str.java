
/*
 * @lc app=leetcode.cn id=28 lang=java
 *
 * [28] 实现 strStr()
 */
class Solution {
    public int strStr(String haystack, String needle) {
        int len = needle.length();
        if (len == 0) {
            return 0;
        }
        String substr;
        int ret = -1;
        for (int i = 0; i < haystack.length() - len + 1; i ++) {
            substr = haystack.substring(i, i + len);
            if (substr.equals(needle)) {
                ret = i;
                break;
            }
        }
        return ret;
    }
}

