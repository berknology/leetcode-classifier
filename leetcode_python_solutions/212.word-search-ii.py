#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start

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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)    
        self.ans = []
        node = trie.root
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtrack(board, i, j, [], node)
        return self.ans
    
    def backtrack(self, board, i, j, path, node):
        if node.is_word:
            self.ans.append(''.join(path))
            node.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or not board[i][j]:
            return False
        child_node = node.children.get(board[i][j])
        if not child_node:
            return False
        temp = board[i][j]
        board[i][j] = None
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            self.backtrack(board, x, y, path+[temp], child_node)
        board[i][j] = temp
    

# @lc code=end

