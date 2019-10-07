#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.minv = []
        

    def push(self, x: int) -> None:
        self.st.append(x)
        if not self.minv:
            self.minv.append(x)
        else:
            self.minv.append(min(self.minv[-1], x))

    def pop(self) -> None:
        self.st.pop()
        self.minv.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minv[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

