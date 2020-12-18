"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        hash_table = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            hash_table[level].append(node.val)
            for child in node.children:
                queue.append((child, level+1))
        return hash_table.values()
