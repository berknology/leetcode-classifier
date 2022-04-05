class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.lcs(word1, word2, 0, 0, {})
        return len(word1)+len(word2)-2*lcs 
    
    def lcs(self, word1, word2, i1, i2, memo):
        if i1 == len(word1) or i2 == len(word2):
            return 0
        if (i1, i2) not in memo:
            if word1[i1] == word2[i2]:
                ans = 1 + self.lcs(word1, word2, i1+1, i2+1, memo)
            else:
                ans = max(self.lcs(word1, word2, i1, i2+1, memo), self.lcs(word1, word2, i1+1, i2, memo))
            memo[(i1, i2)] = ans
        return memo[(i1, i2)]
