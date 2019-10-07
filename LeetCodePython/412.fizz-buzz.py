#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = [str(x) for x in range(1, n + 1)]
        for i in range(2, n, 3):
            ret[i] = "Fizz"
        for i in range(4, n, 5):
            if ret[i] == "Fizz":
                ret[i] += "Buzz"
            else:
                ret[i] = "Buzz"
        return ret
# @lc code=end

