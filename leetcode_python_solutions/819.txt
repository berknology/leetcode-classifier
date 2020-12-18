class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[float('inf')]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]+1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][0]+1)
        return min(dp[-1][0], dp[-1][1])

        
        
"""
A                                
B

dp[i] is the minimum number of swaps between A[:i+1] and B[:i+1]


Case 1:
A[i-1] < B[i]
B[i-1] < A[i]

Cas2:
A[i-1] < A[i]
B[i-1] < B[i]


[1, 3,  5,  4]
[1, 2,  3,  7]


"""
