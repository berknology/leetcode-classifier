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


"""
Time complexity: O(V+E), where V is the number of vertices and E is the number of edges
Space complexity: O(V)
"""