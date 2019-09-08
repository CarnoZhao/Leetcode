import java.util.Dictionary;

/*
 * @lc app=leetcode.cn id=38 lang=java
 *
 * [38] 报数
 */
class Solution {
    public String countAndSay(int n) {
        String x = "1";
        for (int i = 0; i < n - 1; i ++) {
            x = nextInt(x);
        }
        return x;
    }

    private String nextInt(String x) {
        char pre = ' ';
        int cnt = 0;
        String ret = "";
        for (char c : x.toCharArray()) {
            if (c == pre) {
                cnt ++;
            } else if (pre == ' ') {
                pre = c;
                cnt = 1;
            } else {
                ret += String.valueOf(cnt) + String.valueOf(pre);
                pre = c;
                cnt = 1;
            }
        }
        ret += String.valueOf(cnt) + String.valueOf(pre);
        return ret;
    }
}

