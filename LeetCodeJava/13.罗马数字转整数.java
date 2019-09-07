/*
 * @lc app=leetcode.cn id=13 lang=java
 *
 * [13] 罗马数字转整数
 */
class Solution {
    public int romanToInt(String s) {
        int ret = 0;
        char pre = ' ';
        char now;
        for (int i = 0; i < s.length(); i ++) {
            now = s.charAt(i);
            if (i == 0) {
                ret += mapping(now);
                pre = now;
            } else if (mapping(pre) < mapping(now)) {
                ret += mapping(now) - 2 * mapping(pre);
            } else {
                ret += mapping(now);
                pre = now;
            }
        }
        return ret;
    }

    private int mapping(char c) {
        int ret = 0;
        switch (c) {
            case 'I':
                ret += 1;
                break;
            case 'V':
                ret += 5;
                break;
            case 'X':
                ret += 10;
                break;
            case 'L':
                ret += 50;
                break;
            case 'C':
                ret += 100;
                break;
            case 'D':
                ret += 500;
                break;
            case 'M':
                ret += 1000;
                break;
            default:
                break;
        }
        return ret;
    }
}

