class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return m+n-2*dp[-1][-1]


"""
Idea: use DP to find the longest common subsequence
Time complexity: O(mn), where m is the length of word1, n is the length of word2
Space complexity: O(mn)
"""