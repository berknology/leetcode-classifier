import collections
class  TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self._insert(word)
    
    def _insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
    
    def _search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for d in range(26):
                new_c = chr(ord('a') + d)
                if new_c != searchWord[i]:
                    new_word = searchWord[:i] + new_c + searchWord[i+1:]
                    if self._search(new_word):
                        return True
        return False
