class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder = []
        self.dfs(root, inorder)
        left, right = 0, len(inorder)-1
        while left < right:
            _sum = inorder[left] + inorder[right]
            if _sum == k:
                return True
            elif _sum < k:
                left += 1
            else:
                right -= 1
        return False
    
    def dfs(self, root, inorder):
        if not root: return
        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)
    
