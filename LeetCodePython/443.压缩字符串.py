#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 0
        j = 0
        pre = None
        for c in chars:
            if pre == None or c == pre:
                cnt += 1
            elif c != pre:
                chars[j] = pre
                j += 1
                if cnt != 1:
                    while cnt >= 10:
                        chars[j] = str(cnt // 10)
                        cnt %= 10
                        j += 1
                    chars[j] = str(cnt)
                    j += 1
                cnt = 1
            pre = c
        chars[j] = pre
        j += 1
        if cnt != 1:
            while cnt >= 10:
                chars[j] = str(cnt // 10)
                cnt %= 10
                j += 1
            chars[j] = str(cnt)
            j += 1
        return j
                
# @lc code=end

