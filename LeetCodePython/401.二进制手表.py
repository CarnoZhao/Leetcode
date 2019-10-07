#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        import itertools
        ret = []
        for hnum in range(num + 1):
            mnum = num - hnum
            houts = []
            mouts = []
            for h in itertools.combinations((1, 2, 4, 8), hnum):
                sums = sum(h)
                if sums < 12:
                    houts.append(sums)
            for m in itertools.combinations((1, 2, 4, 8, 16, 32), mnum):
                sums = sum(m)
                if sums < 60:
                    mouts.append(sums)
            for h in houts:
                for m in mouts:
                    ret.append(str(h) + ":" + ("0" if m < 10 else "") + str(m))
        return ret
    


# @lc code=end

