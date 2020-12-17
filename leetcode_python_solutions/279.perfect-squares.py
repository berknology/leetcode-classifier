#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        visited = set()
        queue = collections.deque([(n, 0)])
        while queue:
            num, step = queue.popleft()
            if num == 0: return step
            for i in range(1, int(num**0.5)+1):
                if num-i**2 not in visited:
                    visited.add(num-i**2)
                    queue.append((num-i**2, step+1))
            
# @lc code=end

