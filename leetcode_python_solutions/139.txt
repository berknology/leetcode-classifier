class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        return self.word_break(s, word_set, index=0, memo=dict())
    
    def word_break(self, s, word_set, index, memo):
        if index == len(s):
            return True
        if index in memo:
            return memo[index]
        for i in range(index, len(s)):
            word = s[index:i+1]
            if word in word_set and self.word_break(s, word_set, i+1, memo):
                memo[index] = True
                return memo[index]
        memo[index] = False
        return memo[index]

        
