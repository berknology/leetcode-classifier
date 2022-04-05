class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         return self.lcs(text1, text2, len(text1) - 1, len(text2) - 1, {})
#
#     def lcs(self, text1, text2, i, j, memo):
#         if i < 0 or j < 0:
#             return 0
#         if (i, j) not in memo:
#             if text1[i] == text2[j]:
#                 memo[(i, j)] = 1 + self.lcs(text1, text2, i - 1, j - 1, memo)
#             else:
#                 memo[(i, j)] = max(self.lcs(text1, text2, i, j - 1, memo), self.lcs(text1, text2, i - 1, j, memo))
#
#         return memo[(i, j)]