class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        memo = dict()
        for i in range(2, len(A)):
            ans += self.n_slices(A, i, memo)
        return ans
        
    def n_slices(self, A, index, memo):
        if index < 2:
            return 0
        if index in memo:
            return memo[index]
        ans = 0
        if A[index] - A[index-1] == A[index-1] - A[index-2]:
            ans = 1 + self.n_slices(A, index-1, memo)
        memo[index] = ans
        return ans

        
"""
DP

Top down with memo
"""
