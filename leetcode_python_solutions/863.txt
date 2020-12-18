class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.build_graph(root, None)
        queue = collections.deque([(target, 0)])
        visited = set([target])
        ans = []
        while queue:
            node, step = queue.popleft()
            if step == K:
                ans.append(node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, step+1))
        return ans
    def build_graph(self, root, par):
        if not root: return
        neighbors = []
        if par: neighbors.append(par)
        if root.left: neighbors.append(root.left)
        if root.right: neighbors.append(root.right)
        root.neighbors = neighbors
        self.build_graph(root.left, root)
        self.build_graph(root.right, root)
