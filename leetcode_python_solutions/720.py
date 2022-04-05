import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        max_len = 0
        ans = ''
        for word in words:
            if len(word) < max_len:
                continue
            node = trie.root
            for i in range(len(word)):
                if word[i] not in node.children:
                    break
                node = node.children[word[i]]
                if not node.is_word:
                    break
            if i == len(word)-1:
                if len(word) > max_len:
                    max_len = len(word)
                    ans = word
                elif len(word) == max_len and word < ans:
                    ans = word
        return ans
