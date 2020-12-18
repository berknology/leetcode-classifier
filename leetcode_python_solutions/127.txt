class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i, c in enumerate(word):
                for d in range(26):
                    new_c = chr(ord('a') + d)
                    if new_c != c:
                        new_word = word[:i]+new_c+word[i+1:]
                        if new_word in word_set:
                            queue.append((new_word, step+1))
                            word_set.remove(new_word)            
        return 0
        
        
"""
shortest transformation

BST

queue




"""
