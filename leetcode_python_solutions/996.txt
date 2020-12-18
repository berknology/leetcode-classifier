class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.ans = 0
        A.sort()
        visited = [False]*len(A)
        self.backtrack(A, visited, [])
        return self.ans
    def backtrack(self, A, visited, path):
        if len(path) == len(A):
            self.ans += 1
            return 
        for i, num in enumerate(A):
            if not visited[i]:
                if i > 0 and not visited[i-1] and A[i] == A[i-1]:
                    continue
                if not path or int((path[-1] + num)**0.5) == (path[-1] + num)**0.5:
                    visited[i] = True
                    self.backtrack(A, visited, path+[num])
                    visited[i] = False
