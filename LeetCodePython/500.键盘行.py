#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        ]
        ret = []
        for w in words:
            if any([all([c in l for c in w.lower()]) for l in lines]):
                ret.append(w)
        return ret
# @lc code=end

