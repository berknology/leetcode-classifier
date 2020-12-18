class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        return self.search_partial(word, node)
    
    def search_partial(self, word, node) -> bool:
        for i, c in enumerate(word):
            if c != '.':
                if c not in node.children:
                    return False
                node = node.children[c]
            else:
                for l in node.children:
                    child = node.children[l]
                    if self.search_partial(word[i+1:], child):
                        return True
                return False
        return node.is_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
