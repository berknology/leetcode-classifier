class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.top_down(word1, word2, len(word1)-1, len(word2)-1, {})
    
    def top_down(self, word1, word2, idx1, idx2, memo):
        if idx1 == -1 and idx2 == -1:
            return 0
        elif idx1 == -1:
            return idx2+1
        elif idx2 == -1:
            return idx1+1
        if (idx1, idx2) not in memo:
            ans = float('inf')
            if word1[idx1] == word2[idx2]:
                ans = self.top_down(word1, word2, idx1-1, idx2-1, memo)
            else:
                # delete   ab   a
                ans = min(ans, 1 + min(self.top_down(word1, word2, idx1-1, idx2, memo), self.top_down(word1, word2, idx1, idx2-1, memo)))
                # insert  a  ab
                ans = min(ans, 1 + min(self.top_down(word1, word2, idx1, idx2-1, memo), self.top_down(word1, word2, idx1-1, idx2, memo)))
                # replace ac ab
                ans = min(ans, 1 + self.top_down(word1, word2, idx1-1, idx2-1, memo))
            memo[(idx1, idx2)] = ans
        return memo[(idx1, idx2)]
