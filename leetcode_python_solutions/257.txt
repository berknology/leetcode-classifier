class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        self.ans = []
        self.dfs(root, [])
        return self.ans
    
    def dfs(self, root, path):
        if not root: return
        path.append(root.val)
        if not root.left and not root.right:
            self.ans.append('->'.join(map(str, path[:])))
        else:
            self.dfs(root.left, path)
            self.dfs(root.right, path)
        path.pop()
