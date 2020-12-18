class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        self.dfs(root, sum, [])
        return self.ans
    def dfs(self, root, sum, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and root.val == sum:
            self.ans.append(path[:])
        else:
            self.dfs(root.left, sum-root.val, path)
            self.dfs(root.right, sum-root.val, path)
        path.pop()
        
