#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper()
        ret = []
        S = S.replace('-', '')
        while S != '':
            ret.append(S[-K:])
            S = S[:-K]
        ret = ret[::-1]
        return '-'.join(ret)
            
# @lc code=end

