#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.value = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.hash_table = dict()

    def insert(self, key: str, val: int) -> None:
        diff = val - self.hash_table.get(key, 0)
        self.hash_table[key] = val
        node = self.root
        for c in key:
            node = node.children[c]
            node.value += diff

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            node = node.children[c]
        return node.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

