class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        N = len(M)
        ans = 0
        for i in range(N):
            if M[i][i] == 1:
                self.dfs(M, i, N)
                ans += 1
        return ans
    
    def dfs(self, M, i, N):
        M[i][i] = 0
        for j in range(N):
            if M[i][j] == 1:
                M[i][j] = 0
                M[j][i] = 0
                self.dfs(M, j, N)
