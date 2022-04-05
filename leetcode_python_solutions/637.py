class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        hash_table = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            hash_table[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return [sum(hash_table[level])/len(hash_table[level]) for level in hash_table]
        
