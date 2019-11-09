#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        st = [(sr, sc)]
        orig = image[sr][sc]
        if orig == newColor:
            return image
        while st:
            r, c = st[-1]
            image[r][c] = newColor
            if self.check(r - 1, c, image, orig):
                st.append((r - 1, c))
            elif self.check(r, c - 1, image, orig):
                st.append((r, c - 1))
            elif self.check(r + 1, c, image, orig):
                st.append((r + 1, c))
            elif self.check(r, c + 1, image, orig):
                st.append((r, c + 1))
            else:
                st.pop()
        return image

    def check(self, r, c, img, orig):
        R = len(img); C = len(img[0])
        return 0 <= r < R and 0 <= c < C and img[r][c] == orig and (r, c)
# @lc code=end

