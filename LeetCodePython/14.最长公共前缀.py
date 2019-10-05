#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lens = [len(string) for string in strs]
        ref = strs[lens.index(min(lens))]
        ret = ""
        for i, char in enumerate(ref):
            if all([string[i] == char for string in strs]):
                ret += char
            else:
                break
        return ret
# @lc code=end

