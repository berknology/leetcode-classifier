class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            ans[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ans.values()
