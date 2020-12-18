class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2, 0, 0, {})
    
    def lcs(self, text1, text2, idx1, idx2, memo):
        if idx1 == len(text1) or idx2 == len(text2):
            return 0
        if (idx1, idx2) not in memo:
            if text1[idx1] == text2[idx2]:
                ans = 1 + self.lcs(text1, text2, idx1+1, idx2+1, memo)
            else:
                ans = max(self.lcs(text1, text2, idx1, idx2+1, memo), self.lcs(text1, text2, idx1+1, idx2, memo))
            memo[(idx1, idx2)] = ans
        return memo[(idx1, idx2)]
