/*
 * @lc app=leetcode.cn id=58 lang=java
 *
 * [58] 最后一个单词的长度
 */
class Solution {
    public int lengthOfLastWord(String s) {
        String[] splt = s.split(" ");
        if (splt.length == 0) {
            return 0;
        } else {
            return splt[splt.length - 1].length();
        }
    }
}

