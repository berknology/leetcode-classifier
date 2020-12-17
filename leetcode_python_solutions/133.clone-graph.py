#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        self.hash_table = dict()
        return self.clone_graph(node)

    def clone_graph(self, node):
        if node in self.hash_table:
            return self.hash_table[node]
        cloned_node = Node(node.val)
        self.hash_table[node] = cloned_node
        for nei in node.neighbors:
            cloned_node.neighbors.append(self.clone_graph(nei))
        return cloned_node
    
# @lc code=end

