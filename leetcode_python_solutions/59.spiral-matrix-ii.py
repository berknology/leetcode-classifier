#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        index = 1
        i, j = 0, 0
        for _ in range(n**2):
            ans[i][j] = index
            index += 1
            x, y = i+direction[d][0], j+direction[d][1]
            if 0 <= x < n and 0 <= y < n and ans[x][y] == 0:
                i, j = x, y
            else:
                d = (d+1)%4
                i, j = i+direction[d][0], j+direction[d][1]
        return ans
        
# @lc code=end

