#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        queue = collections.deque()
        n = len(A)
        i, j = self.find_first_entry(A)
        A[i][j] = 0
        self.dfs(queue, A, i, j)

        while queue:
            i, j, dis = queue.popleft()
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < n and 0 <= y < n:
                    if A[x][y] == 1: 
                        return dis
                    elif A[x][y] == 0:
                        A[x][y] = 2
                        queue.append((x, y, dis+1))

    def find_first_entry(self, A):
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    return (i, j)

    def dfs(self, queue, A, i, j):
        n = len(A)
        queue.append((i, j, 0))
        for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
            if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                A[x][y] = 0
                self.dfs(queue, A, x, y)       

# @lc code=end

