class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.is_balanced = True
        self.find_height(root)
        return self.is_balanced
    def find_height(self, root):
        if not root: return 0
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        if abs(left_height - right_height) > 1:
            self.is_balanced = False
        return 1 + max(left_height, right_height)
