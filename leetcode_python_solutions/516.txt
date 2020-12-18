class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        new_s = s[::-1]
        return self.lcs(s, new_s, 0, 0, {})
    
    def lcs(self, s1, s2, idx1, idx2, memo):
        if idx1 == len(s1) or idx2 == len(s2):
            return 0
        if (idx1, idx2) not in memo:
            if s1[idx1] == s2[idx2]:
                ans = 1 + self.lcs(s1, s2, idx1+1, idx2+1, memo)
            else:
                ans = max(self.lcs(s1, s2, idx1, idx2+1, memo), self.lcs(s1, s2, idx1+1, idx2, memo))
            memo[(idx1, idx2)] = ans
        return memo[(idx1, idx2)]

        
"""

bbbab
babbb

Longest common sebsequence (LCS)

"""
