#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image, i, j, old_color, new_color):
        image[i][j] = new_color
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == old_color:
                self.dfs(image, x, y, old_color, new_color)

# @lc code=end

