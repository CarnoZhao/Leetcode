#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        dic = {}
        for n in nums2:
            if not st:
                st.append(n)
            if n < st[-1]:
                st.append(n)
            else:
                while st and st[-1] < n:
                    out = st.pop()
                    dic[out] = n
                st.append(n)
        return [dic[n] if n in dic else -1 for n in nums1]
# @lc code=end

