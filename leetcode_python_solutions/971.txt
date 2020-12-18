class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        q = []
        n = len(A)
        i, j = self.return_first_index(A)
        self.dfs(A, i, j, q)
        queue = collections.deque(q)
        while queue:
            i, j, step = queue.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < n and A[x][y] != -1:
                    if A[x][y] == 1:
                        return step
                    A[x][y] = -1
                    queue.append((x, y, step+1))
        
    def return_first_index(self, A):
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    return i, j
    
    def dfs(self, A, i, j, q):
        n = len(A)
        q.append((i, j, 0))
        A[i][j] = -1
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                self.dfs(A, x, y, q)
        
        
        
        
"""
DFS + BFS



"""
