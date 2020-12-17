#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            if word == endWord: return step
            for i in range(len(word)):
                for diff in range(26):
                    char = chr(ord('a') + diff)
                    if char != word[i]:
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in words:
                            queue.append((new_word, step+1))
                            words.remove(new_word)
        return 0
        
# @lc code=end

