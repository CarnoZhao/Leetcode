/*
 * @lc app=leetcode.cn id=38 lang=java
 *
 * [38] 报数
 */
class Solution {
    public String countAndSay(int n) {
        String x = "1";
        for (int i = 0; i < n; i ++) {
            x = nextInt(x);
        }
        return x;
    }

    private String nextInt(String x) {
        String ret = "";
        char pre;
        char now;
        int cnt = 0;
        pre = ' ';
        for (int i = 0; i < x.length(); i ++) {
            now = x.charAt(i);
            if (pre == ' ') {
                pre = now;
                cnt = 1;
            } else if (now == pre) {
                cnt += 1;
            } else {
                ret = cnt + String.valueOf(pre) + ret;
                pre = now;
                cnt = 1;
            }
        }
        ret = cnt + pre + ret;
        return ret;
    }
}

