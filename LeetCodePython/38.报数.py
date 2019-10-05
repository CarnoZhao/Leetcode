#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        ret = '1'
        for i in range(1, n):
            tmp = ''
            pre = None
            cnt = 0
            for char in ret:
                if pre == None or char == pre:
                    cnt += 1
                elif char != pre:
                    tmp += str(cnt) + pre
                    cnt = 1
                pre = char
            ret = tmp + str(cnt) + pre
        return ret
# @lc code=end

