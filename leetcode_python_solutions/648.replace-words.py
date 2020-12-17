#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start

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
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.strip().split()
        for i, word in enumerate(words):
            node = trie.root
            for j in range(len(word)):
                if word[j] not in node.children:
                    break
                node = node.children[word[j]]
                if node.is_word:
                    words[i] = word[:j+1]
                    break

        return ' '.join(words)

# @lc code=end

